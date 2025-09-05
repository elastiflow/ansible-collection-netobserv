from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json

import pytest
from ansible.module_utils import basic
from ansible.module_utils.common.text.converters import to_bytes

from plugins.modules.ensure_single_config_source import get_by_dot, run_module, valid

# "testing" is present in Ansible 2.19+
try:
    from ansible.module_utils import testing

    ansible_new = True
except ImportError:
    pass


def set_module_args(args):
    """prepare arguments so that they will be picked up during module creation"""
    args = json.dumps({"ANSIBLE_MODULE_ARGS": args})
    basic._ANSIBLE_ARGS = to_bytes(args)


@pytest.mark.parametrize(
    ("d", "key", "want"),
    [
        (
            {
                "netobserv_flow_config_processor_enrich_app": {
                    "ipport_config_values": {},
                    "ipport_config_path": "foo",
                },
            },
            "netobserv_flow_config_processor_enrich_app.ipport_config_path",
            "foo",
        ),
    ],
)
def test_get_by_dot(d, key, want):
    assert get_by_dot(d, key) == want


@pytest.mark.parametrize(
    ("vals", "path", "want"),
    [
        ({"bar": "baz"}, "foo", False),
        ({}, "foo", True),
        ({"bar": "baz"}, None, True),
        ({}, None, True),
    ],
)
def test_valid(vals, path, want):
    assert valid(vals, path) == want


@pytest.mark.parametrize(
    ("config_values", "config_path", "ansible_vars", "want"),
    [
        (
            "netobserv_flow_config_processor_enrich_app.ipport_config_values",
            "netobserv_flow_config_processor_enrich_app.ipport_config_path",
            {
                "netobserv_flow_config_processor_enrich_app": {
                    "ipport_config_values": {"bar": "baz"},
                    "ipport_config_path": "foo",
                },
            },
            1,
        ),
        (
            "netobserv_flow_config_processor_enrich_app.ipport_config_values",
            "netobserv_flow_config_processor_enrich_app.ipport_config_path",
            {
                "netobserv_flow_config_processor_enrich_app": {
                    "ipport_config_values": {},
                    "ipport_config_path": "foo",
                },
            },
            0,
        ),
        (
            "netobserv_flow_config_processor_enrich_app.ipport_config_values",
            "netobserv_flow_config_processor_enrich_app.ipport_config_path",
            {
                "netobserv_flow_config_processor_enrich_app": {
                    "ipport_config_values": {"bar": "baz"},
                    "ipport_config_path": None,
                },
            },
            0,
        ),
        (
            "netobserv_flow_config_processor_enrich_app.ipport_config_values",
            "netobserv_flow_config_processor_enrich_app.ipport_config_path",
            {
                "netobserv_flow_config_processor_enrich_app": {
                    "ipport_config_values": {},
                    "ipport_config_path": None,
                },
            },
            0,
        ),
    ],
)
def test_run_module(mocker, config_values, config_path, ansible_vars, want):
    mocked_fail = mocker.patch.object(basic.AnsibleModule, "fail_json")
    mocker.patch.object(basic.AnsibleModule, "exit_json")

    if ansible_new:
        with testing.patch_module_args(
            {
                "config_values": config_values,
                "config_path": config_path,
                "vars": ansible_vars,
            },
        ):
            run_module()
            assert mocked_fail.call_count == want
    else:
        set_module_args(
            {
                "config_values": config_values,
                "config_path": config_path,
                "vars": ansible_vars,
            },
        )

        run_module()
        assert mocked_fail.call_count == want


@pytest.mark.parametrize(
    ("config_values", "config_path", "ansible_vars", "want"),
    [
        (
            "netobserv_flow_config_processor_enrich.aaaa",
            "netobserv_flow_config_processor_enrich.bbbb",
            {
                "netobserv_flow_config_processor_enrich_app": {
                    "ipport_config_values": {"bar": "baz"},
                    "ipport_config_path": "foo",
                },
            },
            SystemExit,
        ),
        (
            "netobserv_flow_config_processor_enrich_app.ipport_config_values",
            "netobserv_flow_config_processor_enrich_app.ipport_config_path",
            {
                "netobserv_flow_config_processor_enrich_app": {
                    "ipport_config_values": None,
                    "ipport_config_path": "foo",
                },
            },
            SystemExit,
        ),
    ],
)
def test_run_module_exception(config_values, config_path, ansible_vars, want):
    if ansible_new:
        with (
            testing.patch_module_args(
                {
                    "config_values": config_values,
                    "config_path": config_path,
                    "vars": ansible_vars,
                },
            ),
            pytest.raises(want),
        ):
            run_module()
    else:
        set_module_args(
            {
                "config_values": config_values,
                "config_path": config_path,
                "vars": ansible_vars,
            },
        )

        with pytest.raises(want):
            run_module()
