<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: elastiflow.netobserv.netobserv_flow
Version: 0.5.1

NetObserv Flow role for ElastiFlow - installs and configures the flow collector.


## Requirements

| Platform | Versions |
| -------- | -------- |
| EL | 8, 9 |
| Ubuntu | jammy, noble |

## Role Arguments


### Entrypoint: main

NetObserv Flow role, configuring flow collection, enrichment, and output for ElastiFlow.


NetObserv Flow role, configuring flow collection, enrichment, and output for ElastiFlow.
Please see full documentation at https://docs.elastiflow.com/flowcoll/configuration

#### License

You need explicitly accept the ElastiFlow license to use NetObserv Flow.
```yaml
netobserv_flow_config_values:
    EF_LICENSE_ACCEPTED: true
```

If you have a license key, please add it to the playbook vars (consider using [Ansible Vault](https://docs.ansible.com/ansible/latest/vault_guide/index.html) to encrypt the license key)
```yaml
netobserv_flow_license:
    license_key: "${LICENSE_KEY}"
    account_id: "${ACCOUNT_ID}"
```

#### User Defined data

For various features you may need to upload user-defined data, for example for:

- [User-defined metadata enrichment](https://docs.elastiflow.com/snmpcoll/configuration/enrichment-options-1/enrich_ip_udm/enrich_ip_udm#ef_processor_enrich_ipaddr_metadata_userdef_path)
- [GeoIP include/exclude](https://docs.elastiflow.com/flowcoll/configuration/enrichment-options/ip-address-enrichment/enrich_ip_maxmind#ef_processor_enrich_ipaddr_maxmind_geoip_inclexcl_path)

The role does not provide a mechanism for uploading local files, nor does it allow defining inline data for those features. However, you may use the following example task (`pre_tasks`) to upload those files from your Ansible control node to the managed host.

```yaml
  post_tasks:
    - name: Copy NetObserv Flow User-Defined Metadata IP enrichment config
      ansible.builtin.copy:
        src: "{{ playbook_dir }}/ipaddrs-test.yaml"
        dest: "/etc/elastiflow/metadata/ipaddrs.yml"
        mode: "0644"
        backup: true
      notify:
        - Restart NetObserv Flow
```

#### Sample flows from the host

You may ingest flows from the server the netobserv-flow is running on by setting-up a [softflowd](https://github.com/irino/softflowd) (available in Debian/Ubuntu repos).
You may install it manually or use following task (full examples may be found in the `examples` dir)
```yaml
tasks:
  - name: Install softflowd
    notify: Restart softflowd
    when: ansible_os_family | lower == "debian"
    block:
      - name: Install softflowd
        ansible.builtin.package:
          name: softflowd
      - name: Configure softflowd
        # -n localhost:port should be identical to `netobserv_flow_config_input_flow.server_udp_port` netobserv-flow var, default is 9995
        # More details on the config here: https://docs.elastiflow.com/additional-resources-reference-articles/guides/configuring-flow-logs-on-devices/device_flow_openwrt_softflowd
        ansible.builtin.copy:
          dest: /etc/softflowd/default.conf
          backup: true
          owner: root
          group: root
          mode: "0644"
          content: |
            interface='any'
            # -n localhost:port should be identical to `netobserv_flow_config_input_flow.server_udp_port` netobserv-flow var, default is 9995
            # Run `softflowd -h` for command-line options details.
            # More details on the config here: https://docs.elastiflow.com/additional-resources-reference-articles/guides/configuring-flow-logs-on-devices/device_flow_openwrt_softflowd
            options='-n localhost:9995
              -v 9
              -L 255
              -T ether
              -6
              -s 1
              -t tcp.fin=10
              -t expint=10
              -t icmp=20
              -t tcp=60
              -t maxlife=60
              -t general=60
              -t udp=60'
```

## Upgrade notes

### v0.4.1 -> v0.5.x

Refer to the [Pull Request](https://github.com/elastiflow/ansible-collection-netobserv/pull/29) for the full list of changes.

- License needs to be explicitly accepted via `netobserv_flow_config_values` (`netobserv_flow_license.accepted`) is removed
  ```yaml
  netobserv_flow_config_values:
    EF_LICENSE_ACCEPTED: true
  ```
- Top-level `netobserv_flow_dashboards` var is removed, OpenSearch and ElasticSearch import dashboard options are now in the `netobserv_flow_output_elasticsearch.dashboards`/`netobserv_flow_output_opensearch.dashboards`
- Update `netobserv_flow_output_elasticsearch`/`netobserv_flow_output_opensearch` variables (refer the role's readme for the details)
- Fill all values that are not present in the "complex" Ansible vars to the `netobserv_flow_config_values` dict.

Please see the example playbooks changes for reference:
- [Example ElasticSearch playbook](https://github.com/elastiflow/ansible-collection-netobserv/pull/29/changes#diff-34614fb12163c3dbf55c7dcc616780f464787d64c58e5dade1f45f10c24c7641)
- [Example OpensearchSearch playbook](https://github.com/elastiflow/ansible-collection-netobserv/pull/29/changes#diff-858969464991d766dda4f3ed2f0503b0bb0b17dac21f331e2e2c0174ff5a0909)

The safest way to upgrade is:
1. Backup `/etc/elastiflow` directory
2. Copy `/etc/elastiflow/flowcoll.yml` values under the the `netobserv_flow_config_values` Ansible variable

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| netobserv_flow_install | Whether to install NetObserv Flow. | bool | no | `True` |
| netobserv_flow_version | NetObserv Flow version to install. | str | no | `1:7.20.0-1` |
| netobserv_flow_config_dir | Directory for NetObserv Flow configuration files. | str | no | `/etc/elastiflow` |
| netobserv_flow_config_file | Main configuration file for NetObserv Flow. | str | no | `{{ netobserv_flow_config_dir }}/flowcoll.yml` |
| netobserv_flow_license | License configuration for NetObserv Flow collector. See: https://docs.elastiflow.com/flowcoll/configuration/config_gen/license ***defaults_prefix:"__"*** | dict of `netobserv_flow_license` [options](#options-for-main--netobserv_flow_license) | no |  |
| netobserv_flow_output_elasticsearch | ElasticSearch output configuration. See: https://docs.elastiflow.com/flowcoll/configuration/outputs/output_elasticsearch/elastic-configuration-options ***defaults_prefix:"__"*** | dict of `netobserv_flow_output_elasticsearch` [options](#options-for-main--netobserv_flow_output_elasticsearch) | no |  |
| netobserv_flow_output_opensearch | OpenSearch output configuration. See: https://docs.elastiflow.com/flowcoll/configuration/outputs/output_opensearch/opensearch-configuration-options ***defaults_prefix:"__"*** | dict of `netobserv_flow_output_opensearch` [options](#options-for-main--netobserv_flow_output_opensearch) | no |  |
| netobserv_flow_config_values | Configuration values for NetObserv Flow. Values are appended to the `flowcoll.yml` as YAML. Example: ```yaml EF_LICENSE_ACCEPTED: "true" EF_SOME_SETTING: "/some/host/path/config.yml" EF_ANOTHER_SETTING: "/some/host/path/config.yml" ``` | dict | no |  |
| netobserv_flow_kernel_parameters | Kernel tuning parameters for NetObserv Flow. See: https://docs.elastiflow.com/flowcoll/installation/requirements#recommended-kernel-tuning ***defaults_prefix:"__"*** | dict of `netobserv_flow_kernel_parameters` [options](#options-for-main--netobserv_flow_kernel_parameters) | no |  |

#### Options for main > netobserv_flow_license

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| account_id | ElastiFlow account ID. | str | no | `None` |
| key | ElastiFlow license key. | str | no | `None` |

#### Options for main > netobserv_flow_output_elasticsearch

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable output to ElasticSearch. | bool | no | `False` |
| ecs | Elastic Common Schema configuration. | dict of `ecs` [options](#options-for-main--netobserv_flow_output_elasticsearch--ecs) | no |  |
| addresses | ElasticSearch node addresses. | str | no | `127.0.0.1:9200` |
| username | Username for ElasticSearch. | str | no | `elastic` |
| password | Password for ElasticSearch. | str | no |  |
| tls | TLS configuration for ElasticSearch output. | dict of `tls` [options](#options-for-main--netobserv_flow_output_elasticsearch--tls) | no |  |
| dashboards | ElasticSearch dashboard import configuration. See: https://docs.elastiflow.com/flowcoll/configuration/outputs/output_elasticsearch | dict of `dashboards` [options](#options-for-main--netobserv_flow_output_elasticsearch--dashboards) | no |  |

#### Options for main > netobserv_flow_output_elasticsearch > ecs

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable Elastic Common Schema. | bool | no | `False` |

#### Options for main > netobserv_flow_output_elasticsearch > tls

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable TLS. | bool | no | `False` |
| skip_verification | Skip certificate verification. | bool | no | `False` |
| ca_cert_filepath | Path to CA certificate. | str | no |  |

#### Options for main > netobserv_flow_output_elasticsearch > dashboards

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable ElasticSearch dashboard import. | bool | no | `False` |
| url | URL for Kibana dashboard. | str | no | `https://raw.githubusercontent.com/elastiflow/elastiflow_for_elasticsearch/master/kibana/flow/kibana-8.14.x-flow-codex.ndjson` |
| override | Override existing dashboards. | bool | no | `True` |
| kibana_url | Kibana server URL. | str | no | `http://127.0.0.1:5601` |
| tls | TLS configuration for dashboard import. | dict of `tls` [options](#options-for-main--netobserv_flow_output_elasticsearch--dashboards--tls) | no |  |

#### Options for main > netobserv_flow_output_elasticsearch > dashboards > tls

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| validate_certs | Validate TLS certificates. | bool | no | `False` |
| client_cert | Path to client certificate. | str | no | `None` |
| client_key | Path to client key. | str | no | `None` |

#### Options for main > netobserv_flow_output_opensearch

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable output to OpenSearch. | bool | no | `False` |
| ecs | Elastic Common Schema configuration. | dict of `ecs` [options](#options-for-main--netobserv_flow_output_opensearch--ecs) | no |  |
| addresses | OpenSearch node addresses. | str | no | `127.0.0.1:9200` |
| username | Username for OpenSearch. | str | no | `admin` |
| password | Password for OpenSearch. | str | no |  |
| tls | TLS configuration for OpenSearch output. | dict of `tls` [options](#options-for-main--netobserv_flow_output_opensearch--tls) | no |  |
| dashboards | OpenSearch dashboard import configuration. See: https://docs.elastiflow.com/flowcoll/configuration/outputs/output_opensearch | dict of `dashboards` [options](#options-for-main--netobserv_flow_output_opensearch--dashboards) | no |  |

#### Options for main > netobserv_flow_output_opensearch > ecs

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable Elastic Common Schema. | bool | no | `False` |

#### Options for main > netobserv_flow_output_opensearch > tls

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable TLS. | bool | no | `False` |
| skip_verification | Skip certificate verification. | bool | no | `False` |
| ca_cert_filepath | Path to CA certificate. | str | no |  |

#### Options for main > netobserv_flow_output_opensearch > dashboards

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable OpenSearch dashboard import. | bool | no | `False` |
| url | URL for OpenSearch dashboard. | str | no | `https://raw.githubusercontent.com/elastiflow/elastiflow_for_opensearch/main/dashboards/flow/dashboards-2.14.x-flow-codex.ndjson` |
| override | Override existing dashboards. | bool | no | `True` |
| dashboards_url | OpenSearch Dashboards URL. | str | no | `http://127.0.0.1:5601` |
| tls | TLS configuration for dashboard import. | dict of `tls` [options](#options-for-main--netobserv_flow_output_opensearch--dashboards--tls) | no |  |

#### Options for main > netobserv_flow_output_opensearch > dashboards > tls

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| validate_certs | Validate TLS certificates. | bool | no | `False` |
| client_cert | Path to client certificate. | str | no | `None` |
| client_key | Path to client key. | str | no | `None` |

#### Options for main > netobserv_flow_kernel_parameters

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| tune_enabled | Enable kernel tuning. | bool | no | `True` |
| net.core.netdev_max_backlog | Maximum number of packets allowed to queue when the interface receives packets faster than the kernel can process them. | int | no | `4096` |
| net.core.rmem_default | Default receive buffer size for network sockets. | int | no | `262144` |
| net.core.rmem_max | Maximum receive buffer size for network sockets. Related to [EF_FLOW_SERVER_UDP_READ_BUFFER_MAX_SIZE](https://docs.elastiflow.com/flowcoll/configuration/inputs/input_udp#ef_flow_server_udp_read_buffer_max_size) | int | no | `33554432` |
| net.ipv4.udp_rmem_min | Minimum receive buffer size for UDP sockets. | int | no | `131072` |
| net.ipv4.udp_mem | Memory usage limits for UDP. | str | no | `2097152 4194304 8388608` |



## Dependencies
- {'role': 'elastiflow.netobserv._collector_install', 'vars': {'version': '{{ netobserv_flow_version }}', 'collector_type': 'netobserv-flow'}, 'when': 'netobserv_flow_install'}

## Example Playbook

```
- hosts: all
  tasks:
    - name: Importing role: elastiflow.netobserv.netobserv_flow
      ansible.builtin.import_role:
        name: elastiflow.netobserv.netobserv_flow
      vars:
```

## License

Apache-2.0

## Author and Project Information
ElastiFlow Engineering Team <engineering@elastiflow.com>

<!-- END_ANSIBLE_DOCS -->
