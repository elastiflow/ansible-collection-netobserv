#!/usr/bin/python

DOCUMENTATION = r"""
---
module: ensure_single_config_source

short_description: Ensures configuration is provided from a single source.

version_added: "0.1.0"

description:
  - This module acts as a validation helper to ensure that configuration is provided from a single, unambiguous source.
  - It enforces a mutual exclusion rule on parameters that define configuration, such as providing values directly versus providing a path to a file.
  - Its primary use is to fail early in a playbook or role if a user has provided a conflicting or ambiguous configuration.
  - The module succeeds if only one configuration source is defined and fails if multiple sources are used, causing to fail early.

options:
  config_values:
    description: A dict key that contains config values (separated by dot)
    type: str
    required: true
  config_path:
    description: A dict key that contains local config path (separated by dot)
    type: str
    required: true
  vars:
    description: The Ansible vars dict to look the `config_values` and `config_path` keys.
    type: dict
    required: true

author: ElastiFlow Engineering Team <engineering@elastiflow.com> (@elastiflow)
"""

EXAMPLES = r"""
- name: This should fail
  elastiflow.netobserv.ensure_single_config_source:
    config_values: netobserv_flow_config_processor_enrich_app.ipport_config_values
    config_path: netobserv_flow_config_processor_enrich_app.ipport_config_local_path
    vars: "{{ vars }}"
  vars:
    netobserv_flow_config_processor_enrich_app:
      ipport_config_values: { foo: "bar" }
      ipport_config_local_path: "fff"

- name: This should pass
  elastiflow.netobserv.ensure_single_config_source:
    config_values: netobserv_flow_config_processor_enrich_app.ipport_config_values
    config_path: netobserv_flow_config_processor_enrich_app.ipport_config_local_path
    vars: "{{ vars }}"
  vars:
    netobserv_flow_config_processor_enrich_app:
      ipport_config_values: { foo: "bar" }
      ipport_config_local_path: null

- name: This should pass
  elastiflow.netobserv.ensure_single_config_source:
    config_values: netobserv_flow_config_processor_enrich_app.ipport_config_values
    config_path: netobserv_flow_config_processor_enrich_app.ipport_config_local_path
    vars: "{{ vars }}"
  vars:
    netobserv_flow_config_processor_enrich_app:
      ipport_config_values: {}
      ipport_config_local_path: null

- name: This should pass
  elastiflow.netobserv.ensure_single_config_source:
    config_values: netobserv_flow_config_processor_enrich_app.ipport_config_values
    config_path: netobserv_flow_config_processor_enrich_app.ipport_config_local_path
    vars: "{{ vars }}"
  vars:
    netobserv_flow_config_processor_enrich_app:
      ipport_config_values: {}
      ipport_config_local_path: "/home/user/config.yml"
"""

import typing  # noqa: E402 # Ansible rule conflicting with Ruff

from ansible.module_utils.basic import AnsibleModule  # noqa: E402 # Ansible rule conflicting with Ruff


def get_by_dot(d: typing.Dict, key: str) -> typing.Any:  # noqa: ANN401
    if "." in key:
        key, rest = key.split(".", 1)
        return get_by_dot(d[key], rest)

    return d[key]


def valid(vals: typing.Dict, path: str) -> bool:
    return not (len(vals) > 0 and path is not None)


def run_module() -> None:
    module_args = {
        "config_values": {"type": "str", "required": True},
        "config_path": {"type": "str", "required": True},
        "vars": {"type": "dict", "required": True},
    }

    result = {"changed": False}
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    config_values_val = None
    config_path_val = None

    try:
        config_values_val = get_by_dot(module.params["vars"], module.params["config_values"])
    except KeyError:
        module.fail_json(msg=f"'dict object' has no attribute '{module.params['config_values']}'", **result)

    if config_values_val is None:
        module.fail_json(msg=f"Variable '{module.params['config_values']}' is None, should be a dict", **result)

    try:
        config_path_val = get_by_dot(module.params["vars"], module.params["config_path"])
    except KeyError:
        module.fail_json(msg=f"'dict object' has no attribute '{module.params['config_path']}'", **result)

    if module.check_mode:
        module.exit_json(**result)

    if not valid(config_values_val, config_path_val):
        msg = (
            f"Both '{module.params['config_values']}' and '{module.params['config_path']}' can not be set.\n"
            f"Set '{module.params['config_values']}' to empty map '{{}}'\n"
            f"Or '{module.params['config_path']}' to 'null'"
        )
        module.fail_json(msg=msg, **result)

    module.exit_json(**result)


def main() -> None:
    run_module()


if __name__ == "__main__":
    main()
    main()
