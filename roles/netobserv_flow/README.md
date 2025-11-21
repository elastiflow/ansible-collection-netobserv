<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: elastiflow.netobserv.netobserv_flow
Version: 0.4.0

NetObserv Flow role for ElastiFlow - installs and configures the flow collector.


## Requirements

| Platform | Versions |
| -------- | -------- |
| EL | 8, 9 |
| Ubuntu | jammy, noble |

## Role Arguments


### Entrypoint: main

NetObserv Flow role, configuring flow collection, enrichment, and output for ElastiFlow.
Please see full documentation for:
* [Common Options](https://www.elastiflow.com/docs/category/configuration-reference/category/common-options)
* [NetObserv Flow exclusive options](https://www.elastiflow.com/docs/category/configuration-reference/category/net-observ-flow)

#### License

If you have a license key, please add it to the playbook vars (consider using [Ansible Vault](https://docs.ansible.com/ansible/latest/vault_guide/index.html) to encrypt the license key)
```yaml
netobserv_flow_config_license:
    license_key: "${LICENSE_KEY}"
    account_id: "${ACCOUNT_ID}"
```


|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| netobserv_flow_install | Whether to install NetObserv Flow. | bool | no | `True` |
| netobserv_flow_version | NetObserv Flow version to install. | str | no | `1:7.19.3-1` |
| netobserv_flow_config_dir | Directory for NetObserv Flow configuration files. | str | no | `/etc/elastiflow` |
| netobserv_flow_validate_vars | Validate variables before applying configuration. | bool | no | `True` |
| netobserv_flow_config_file | Main configuration file for NetObserv Flow. | str | no | `{{ netobserv_flow_config_dir }}/flowcoll.yml` |
| netobserv_flow_config_data_path | Data path for NetObserv Flow runtime data. | str | no | `/var/lib/elastiflow/flowcoll` |
| netobserv_flow_config_license | License configuration for NetObserv Flow collector. See: https://www.elastiflow.com/docs/config_ref/common/license ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_license` [options](#options-for-main--netobserv_flow_config_license) | no |  |
| netobserv_flow_config_logger | Logging configuration for NetObserv Flow collector. See: https://www.elastiflow.com/docs/config_ref/common/logging ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_logger` [options](#options-for-main--netobserv_flow_config_logger) | no |  |
| netobserv_flow_config_api | API server configuration for NetObserv Flow collector. See: https://www.elastiflow.com/docs/config_ref/common/api ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_api` [options](#options-for-main--netobserv_flow_config_api) | no |  |
| netobserv_flow_config_processor | Common processor configuration for NetObserv Flow collector. See: https://www.elastiflow.com/docs/config_ref/common/processor ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_processor` [options](#options-for-main--netobserv_flow_config_processor) | no |  |
| netobserv_flow_config_processor_enrich_totals_if_no_deltas | See: https://www.elastiflow.com/docs/config_ref/flowcoll/enrich_general | bool | no | `False` |
| netobserv_flow_config_processor_enrich_app | See: https://www.elastiflow.com/docs/config_ref/flowcoll/enrich_apps ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_processor_enrich_app` [options](#options-for-main--netobserv_flow_config_processor_enrich_app) | no |  |
| netobserv_flow_config_processor_enrich_ipaddr_dns | IP address DNS enrichment configuration. See: https://www.elastiflow.com/docs/config_ref/flowcoll/enrich_ip_hostname ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_processor_enrich_ipaddr_dns` [options](#options-for-main--netobserv_flow_config_processor_enrich_ipaddr_dns) | no |  |
| netobserv_flow_config_processor_enrich_ipaddr_maxmind | IP address GeoIP enrichment configuration. See: https://www.elastiflow.com/docs/config_ref/flowcoll/enrich_ip_maxmind ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_processor_enrich_ipaddr_maxmind` [options](#options-for-main--netobserv_flow_config_processor_enrich_ipaddr_maxmind) | no |  |
| netobserv_flow_config_processor_enrich_ipaddr_netintel | NetIntel enrichment configuration. See: https://www.elastiflow.com/docs/config_ref/flowcoll/enrich_ip_netintel ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_processor_enrich_ipaddr_netintel` [options](#options-for-main--netobserv_flow_config_processor_enrich_ipaddr_netintel) | no |  |
| netobserv_flow_config_processor_enrich_ipaddr_metadata | User-defined IP metadata enrichment configuration. See: https://www.elastiflow.com/docs/config_ref/flowcoll/enrich_ip_udm/ ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_processor_enrich_ipaddr_metadata` [options](#options-for-main--netobserv_flow_config_processor_enrich_ipaddr_metadata) | no |  |
| netobserv_flow_config_processor_enrich_netif_flow_options_enable | See: https://www.elastiflow.com/docs/config_ref/flowcoll/enrich_netif_options | bool | no | `True` |
| netobserv_flow_config_processor_enrich_netif_snmp | SNMP-based network interface enrichment configuration. See: https://www.elastiflow.com/docs/config_ref/flowcoll/enrich_netif_snmp ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_processor_enrich_netif_snmp` [options](#options-for-main--netobserv_flow_config_processor_enrich_netif_snmp) | no |  |
| netobserv_flow_config_processor_enrich_netif_metadata | User-defined network interface metadata enrichment configuration. See: https://www.elastiflow.com/docs/config_ref/flowcoll/enrich_netif_udm ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_processor_enrich_netif_metadata` [options](#options-for-main--netobserv_flow_config_processor_enrich_netif_metadata) | no |  |
| netobserv_flow_config_processor_enrich_communityid | CommunityID enrichment configuration. See: https://www.elastiflow.com/docs/config_ref/flowcoll/enrich_comcon/#community-id ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_processor_enrich_communityid` [options](#options-for-main--netobserv_flow_config_processor_enrich_communityid) | no |  |
| netobserv_flow_config_processor_enrich_conversationid | ConversationID enrichment configuration. See: https://www.elastiflow.com/docs/config_ref/flowcoll/enrich_comcon/#conversation-id ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_processor_enrich_conversationid` [options](#options-for-main--netobserv_flow_config_processor_enrich_conversationid) | no |  |
| netobserv_flow_config_output_stdout | Stdout output configuration. See: https://www.elastiflow.com/docs/config_ref/common/output_stdout ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_output_stdout` [options](#options-for-main--netobserv_flow_config_output_stdout) | no |  |
| netobserv_flow_config_output_elasticsearch | ElasticSearch output configuration. See: https://www.elastiflow.com/docs/config_ref/common/output_elasticsearch ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_output_elasticsearch` [options](#options-for-main--netobserv_flow_config_output_elasticsearch) | no |  |
| netobserv_flow_config_output_opensearch | OpenSearch output configuration. See: https://www.elastiflow.com/docs/config_ref/common/output_opensearch ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_output_opensearch` [options](#options-for-main--netobserv_flow_config_output_opensearch) | no |  |
| netobserv_flow_config_input_flow | Netflow/IPFIX/sFlow (UDP) input configuration. See: https://www.elastiflow.com/docs/config_ref/flowcoll/input_udp ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_input_flow` [options](#options-for-main--netobserv_flow_config_input_flow) | no |  |
| netobserv_flow_config_input_aws_vpc_flow_log_firehose | AWS VPC Flow Log Firehose input configuration. See: https://www.elastiflow.com/docs/config_ref/flowcoll/input_aws_firehose ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_input_aws_vpc_flow_log_firehose` [options](#options-for-main--netobserv_flow_config_input_aws_vpc_flow_log_firehose) | no |  |
| netobserv_flow_config_input_aws_vpc_flow_log_s3 | AWS VPC Flow Log S3 input configuration. See: https://www.elastiflow.com/docs/config_ref/flowcoll/input_aws_s3 ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_input_aws_vpc_flow_log_s3` [options](#options-for-main--netobserv_flow_config_input_aws_vpc_flow_log_s3) | no |  |
| netobserv_flow_config_input_azure_flow_log_vnet | Azure VNET Flow Log input configuration. See: https://www.elastiflow.com/docs/config_ref/flowcoll/input_azure_vnet ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_input_azure_flow_log_vnet` [options](#options-for-main--netobserv_flow_config_input_azure_flow_log_vnet) | no |  |
| netobserv_flow_config_input_benchmark | Benchmark input configuration. See: https://www.elastiflow.com/docs/config_ref/flowcoll/input_benchmark ***defaults_prefix:"__"*** | dict of `netobserv_flow_config_input_benchmark` [options](#options-for-main--netobserv_flow_config_input_benchmark) | no |  |
| netobserv_flow_custom_config_values | Custom configuration values for NetObserv Flow. Values are appended to the `flowcoll.yml` as YAML. Example: ```yaml EF_SOME_SETTING: "/some/host/path/config.yml" EF_ANOTHER_SETTING: "/some/host/path/config.yml" ``` | dict | no |  |
| netobserv_flow_dashboards | Dashboard import configuration for ElasticSearch and OpenSearch. ***defaults_prefix:"__"*** | dict of `netobserv_flow_dashboards` [options](#options-for-main--netobserv_flow_dashboards) | no |  |
| netobserv_flow_kernel_parameters | Kernel tuning parameters for NetObserv Flow. See: https://www.elastiflow.com/docs/flowcoll/requirements/#recommended-kernel-tuning ***defaults_prefix:"__"*** | dict of `netobserv_flow_kernel_parameters` [options](#options-for-main--netobserv_flow_kernel_parameters) | no |  |

#### Options for main > netobserv_flow_config_license

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| accepted | Accept the ElastiFlow license agreement. | bool | no | `True` |
| account_id | ElastiFlow account ID. | str | no | `None` |
| key | ElastiFlow license key. | str | no | `None` |

#### Options for main > netobserv_flow_config_logger

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| level | Log level (e.g., info, debug, warn, error). | str | no | `info` |
| encoding | Log encoding format. | str | no | `json` |
| file_log_enable | Enable logging to file. | bool | no | `False` |
| file_log_filename | Log file path. | str | no | `/var/log/elastiflow/flowcoll/flowcoll.log` |
| file_log_max_size | Maximum log file size in MB. | int | no | `100` |
| file_log_max_age | Maximum age of log files before rotation. | str | no |  |
| file_log_max_backups | Maximum number of log file backups. | int | no | `4` |
| file_log_compress | Compress rotated log files. | bool | no | `False` |

#### Options for main > netobserv_flow_config_api

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| instance_name | Name of the API instance. | str | no | `{{ ansible_hostname }}` |
| ip | API server IP address. | str | no | `0.0.0.0` |
| port | API server port. | int | no | `8080` |
| tls | TLS configuration for API server. | dict of `tls` [options](#options-for-main--netobserv_flow_config_api--tls) | no |  |
| basic_auth_enable | Enable basic authentication for API. | bool | no | `False` |
| basic_auth_username | Username for basic authentication. | str | no |  |
| basic_auth_password | Password for basic authentication. | str | no |  |

#### Options for main > netobserv_flow_config_api > tls

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable TLS for API server. | bool | no | `False` |
| cert_filepath | Path to TLS certificate file. | str | no |  |
| key_filepath | Path to TLS key file. | str | no |  |

#### Options for main > netobserv_flow_config_processor

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| pool_size | Number of processor threads. | int | no | `0` |
| translate_keep_ids | ID translation mode. | str | no | `default` |
| duration_precision | Duration precision (ms, s, etc.). | str | no | `ms` |
| timestamp_precision | Timestamp precision (ms, s, etc.). | str | no | `ms` |
| percent_norm | Normalization percentage. | int | no | `100` |
| keep_cpu_ticks | Keep CPU tick counters. | bool | no | `False` |
| drop_fields | Fields to drop from records. | str | no |  |
| decode_ipfix_enable | Enable IPFIX decoding. | bool | no | `True` |
| decode_netflow1_enable | Enable NetFlow v1 decoding. | bool | no | `True` |
| decode_netflow5_enable | Enable NetFlow v5 decoding. | bool | no | `True` |
| decode_netflow6_enable | Enable NetFlow v6 decoding. | bool | no | `True` |
| decode_netflow7_enable | Enable NetFlow v7 decoding. | bool | no | `True` |
| decode_netflow9_enable | Enable NetFlow v9 decoding. | bool | no | `True` |
| decode_sflow5_enable | Enable sFlow v5 decoding. | bool | no | `True` |
| decode_sflow_flows_enable | Enable sFlow flows decoding. | bool | no | `True` |
| decode_sflow_flows_keep_samples | Keep sFlow flow samples. | bool | no | `False` |
| decode_sflow_counters_enable | Enable sFlow counters decoding. | bool | no | `True` |
| decode_max_records_per_packet | Maximum records per packet. | int | no | `64` |
| enrich_asn_pref | ASN enrichment preference. | str | no | `lookup` |
| enrich_join_asn | Join ASN enrichment. | bool | no | `True` |
| enrich_join_geoip | Join GeoIP enrichment. | bool | no | `True` |
| enrich_join_netattr | Join network attribute enrichment. | bool | no | `True` |
| enrich_join_subnetattr | Join subnet attribute enrichment. | bool | no | `True` |
| enrich_join_sec | Join security enrichment. | bool | no | `True` |
| expand_clisrv | Expand client/server fields. | bool | no | `True` |
| expand_clisrv_no_l4_ports | Expand client/server fields without L4 ports. | bool | no | `True` |
| ifa_enable | Enable IFA enrichment. | bool | no | `False` |
| ifa_worker_size | IFA worker pool size. | int | no | `None` |
| enrich_samplerate_cache_size | Sample rate cache size. | int | no | `32768` |
| enrich_samplerate_userdef_enable | Enable user-defined sample rate. | bool | no | `False` |
| enrich_samplerate_userdef_path | Path to user-defined sample rate config. | str | no | `/etc/elastiflow/settings/sample_rate.yml` |
| enrich_samplerate_userdef_override | Override sample rate with user-defined config. | bool | no | `False` |
| enrich_samplerate_userdef_config_values | Inline user-defined sample rate config values. Example: ```yaml 192.0.2.1: 1024 192.0.2.2: 512 192.0.2.0-192.0.2.255: 256 192.0.2.0/24: 128  # global sample rate "0.0.0.0/0": 56 ``` | dict | no |  |

#### Options for main > netobserv_flow_config_processor_enrich_app

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| id_enable | Enable application ID enrichment. | bool | no | `False` |
| id_path | Path to application ID config. | str | no | `/etc/elastiflow/app/appid.yml` |
| id_ttl | TTL for application ID cache. | int | no | `7200` |
| ipport_enable | Enable application IP/port enrichment. | bool | no | `False` |
| ipport_path | Path to application IP/port config. | str | no | `/etc/elastiflow/app/ipport.yml` |
| ipport_config_values | Inline application IP/port config values. Example: ```yaml 192.168.1.0/24:   8090:     name: "Synergy-cidr-port"     category: "category-cidr-port"     subcategory: "subcategory-cidr-port"     metadata:       ".location": "austin-cidr-port"       "business.unit": "finance-cidr-port"       "dev.unit": "dev-cidr-port"       "app.count": 27 ``` | dict | no |  |
| ipport_config_local_path | Local path for application IP/port config. | str | no | `None` |
| ipport_ttl | TTL for application IP/port cache. | int | no | `7200` |
| ipport_private | Enable private IP/port enrichment. | bool | no | `True` |
| ipport_public | Enable public IP/port enrichment. | bool | no | `False` |
| refresh_rate | Refresh rate in minutes. | int | no | `15` |

#### Options for main > netobserv_flow_config_processor_enrich_ipaddr_dns

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable DNS enrichment. | bool | no | `False` |
| nameserver_ip | Nameserver IP address. | str | no | `None` |
| nameserver_timeout | Nameserver timeout in milliseconds. | int | no | `3000` |
| resolve_private | Resolve private IP addresses. | bool | no | `True` |
| resolve_public | Resolve public IP addresses. | bool | no | `True` |
| userdef_path | Path to user-defined hostname config. | str | no | `None` |
| userdef_config_values | Inline user-defined hostname config values. Example: ```yaml 192.0.2.1: "host1" 192.0.2.2: "host2" ``` | dict | no |  |
| userdef_config_local_path | Local path for user-defined hostname config. | str | no | `None` |
| userdef_refresh_rate | Refresh rate in minutes for user-defined hostname config. | int | no | `15` |
| inclexcl_path | Path to include/exclude config. | str | no |  |
| inclexcl_config_values | Inline include/exclude config values. Example: ```yaml include:   asn:     - 14168   cidr:     - 10.0.0.0/8     - 192.168.0.0/16 exclude:   #asn:   #  -   cidr:     - 192.168.100.0/24 ``` | dict | no |  |
| inclexcl_config_local_path | Local path for include/exclude config. | str | no | `None` |
| inclexcl_refresh_rate | Refresh rate in minutes for include/exclude config. | int | no | `15` |

#### Options for main > netobserv_flow_config_processor_enrich_ipaddr_maxmind

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| asn_enable | Enable ASN enrichment. | bool | no | `False` |
| asn_path | Path to ASN database. | str | no | `/etc/elastiflow/maxmind/GeoLite2-ASN.mmdb` |
| geoip_enable | Enable GeoIP enrichment. | bool | no | `False` |
| geoip_path | Path to GeoIP database. | str | no | `/etc/elastiflow/maxmind/GeoLite2-City.mmdb` |
| geoip_values | GeoIP values to extract. | str | no | `city,country,country_code,location,timezone` |
| geoip_lang | GeoIP language. | str | no | `en` |
| geoip_inclexcl_path | Path to GeoIP include/exclude config. | str | no |  |
| geoip_inclexcl_config_values | Inline GeoIP include/exclude config values. Example: ```yaml include:   asn:     - 14168   cidr:     - 10.0.0.0/8     - 192.168.0.0/16 exclude:   #asn:   #  -   cidr:     - 192.168.100.0/24 ``` | dict | no |  |
| geoip_inclexcl_config_local_path | Local path for GeoIP include/exclude config. | str | no | `None` |
| geoip_inclexcl_refresh_rate | Refresh rate in minutes for GeoIP include/exclude config. | int | no | `15` |

#### Options for main > netobserv_flow_config_processor_enrich_ipaddr_netintel

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable NetIntel enrichment. | bool | no | `True` |
| as_prefix_precision | It's possible for an Autonomous system to house other Autonomous systems. Therefore, a user can either get the most specific AS prefix or all the prefixes for all the Autonomous systems a packet went through. | str | no | `exact` |
| threat_collection_path | Path to threat collection. | str | no |  |
| ip_db_path | Path to IP database. | str | no |  |

#### Options for main > netobserv_flow_config_processor_enrich_ipaddr_metadata

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable user-defined IP metadata enrichment. | bool | no | `False` |
| userdef_path | Path to user-defined IP metadata config. | str | no | `None` |
| userdef_config_values | Inline user-defined IP metadata config values. Example: ```yaml # Specify whether the IP/CIDR/Range is considered to be "internal". 192.0.2.0/24:   internal: true  # Additional options are name, vlan, tags and metadata. 192.0.2.192/26:   name: atlanta_guest_wifi   vlan: 1001   tags:     - wifi     - dhcp   metadata:     dhcp.pool.name: atlanta_guest_wifi     .site.id: atlanta ``` | dict | no |  |
| userdef_config_local_path | Local path for user-defined IP metadata config. | str | no | `None` |
| refresh_rate | Refresh rate in minutes. | int | no | `15` |
| api_enable | Enable API for managing user-defined IP metadata. | bool | no | `False` |

#### Options for main > netobserv_flow_config_processor_enrich_netif_snmp

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable SNMP enrichment. | bool | no | `False` |
| port | SNMP port. | int | no | `161` |
| version | SNMP version. | int | no | `2` |
| communities | SNMP communities. | str | no | `public` |
| v3_username | SNMP v3 username. | str | no |  |
| v3_authentication_protocol | SNMP v3 authentication protocol. | str | no | `noauth` |
| v3_authentication_passphrase | SNMP v3 authentication passphrase. | str | no |  |
| v3_privacy_protocol | SNMP v3 privacy protocol. | str | no | `nopriv` |
| v3_privacy_passphrase | SNMP v3 privacy passphrase. | str | no |  |
| timeout | SNMP timeout in seconds. | int | no | `2` |
| retries | SNMP retries. | int | no | `1` |

#### Options for main > netobserv_flow_config_processor_enrich_netif_metadata

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable user-defined netif metadata enrichment. | bool | no | `False` |
| userdef_path | Path to user-defined netif metadata config. | str | no | `None` |
| userdef_config_values | Inline user-defined netif metadata config values. Example: ```yaml 10.0.0.1:   1:     ifName: lo     ifDescr: lo     ifAlias: lo     ifType: 24     ifSpeed: 10000000     tags:       - router_mgmt     metadata:       sec.zone.name: network   3:     internal: false     ifName: eth0     ifDescr: eth0     ifAlias: internet     ifType: 6     ifSpeed: 1000000000     cirIn: 200000000     cirOut: 12000000     tags:       - verizon     metadata:       sec.zone.name: internet ``` | dict | no |  |
| userdef_config_local_path | Local path for user-defined netif metadata config. | str | no | `None` |
| refresh_rate | Refresh rate in minutes. | int | no | `15` |

#### Options for main > netobserv_flow_config_processor_enrich_communityid

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable CommunityID enrichment. | bool | no | `True` |
| seed | CommunityID seed value. | int | no | `0` |

#### Options for main > netobserv_flow_config_processor_enrich_conversationid

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable ConversationID enrichment. | bool | no | `True` |
| seed | ConversationID seed value. | int | no | `0` |

#### Options for main > netobserv_flow_config_output_stdout

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable output to stdout. | bool | no | `False` |
| format | Output format. | str | no | `json_pretty` |
| allowed_record_types | Allowed record types for stdout output. | str | no | `as_path_hop,flow_option,flow,ifa_hop,telemetry,metric,log` |

#### Options for main > netobserv_flow_config_output_elasticsearch

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable output to ElasticSearch. | bool | no | `False` |
| ecs_enable | Enable Elastic Common Schema. | bool | no | `False` |
| batch_deadline | Deadline for batch processing in milliseconds. | int | no | `2000` |
| batch_max_bytes | Maximum batch size in bytes. | int | no | `8388608` |
| timestamp_source | Source for event timestamps. | str | no | `collect` |
| index_period | Index period (rollover, daily, etc.). | str | no | `rollover` |
| tsds_enable | Enable time-series data stream. | bool | no | `False` |
| index_suffix | Suffix for index names. | str | no |  |
| index_template_enable | Enable index template management. | bool | no | `True` |
| index_template_overwrite | Overwrite existing index templates. | bool | no | `False` |
| index_template_shards | Number of primary shards for index templates. | int | no | `3` |
| index_template_replicas | Number of replica shards for index templates. | int | no | `1` |
| index_template_refresh_interval | Index refresh interval. | str | no | `10s` |
| index_template_codec | Codec for index template. | str | no | `best_compression` |
| index_template_ilm_lifecycle | ILM lifecycle policy name. | str | no | `elastiflow` |
| index_template_pipeline_default | Default ingest pipeline. | str | no | `_none` |
| index_template_pipeline_final | Final ingest pipeline. | str | no | `_none` |
| addresses | ElasticSearch node addresses. | str | no | `127.0.0.1:9200` |
| username | Username for ElasticSearch. | str | no | `elastic` |
| password | Password for ElasticSearch. | str | no |  |
| cloud | ElasticSearch cloud configuration. | dict of `cloud` [options](#options-for-main--netobserv_flow_config_output_elasticsearch--cloud) | no |  |
| tls | TLS configuration for ElasticSearch output. | dict of `tls` [options](#options-for-main--netobserv_flow_config_output_elasticsearch--tls) | no |  |
| retry_enable | Enable retry on failure. | bool | no | `True` |
| retry_on_timeout_enable | Enable retry on timeout. | bool | no | `True` |
| max_retries | Maximum number of retries. | int | no | `3` |
| retry_backoff | Backoff time between retries (ms). | int | no | `1000` |
| storage_optimization_enable | Enable storage optimization. | bool | no | `True` |
| drop_fields | Fields to drop from output. | str | no |  |
| allowed_record_types | Allowed record types for ElasticSearch output. | str | no | `as_path_hop,flow_option,flow,ifa_hop,telemetry,metric` |

#### Options for main > netobserv_flow_config_output_elasticsearch > cloud

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| id | Cloud ID. | str | no |  |
| api_key | Cloud API key. | str | no |  |

#### Options for main > netobserv_flow_config_output_elasticsearch > tls

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| client_ca_cert_filepath | Path to client CA certificate. | str | no |  |
| client_cert_filepath | Path to client certificate. | str | no |  |
| client_key_filepath | Path to client key. | str | no |  |
| enable | Enable TLS. | bool | no | `False` |
| skip_verification | Skip certificate verification. | bool | no | `False` |
| ca_cert_filepath | Path to CA certificate. | str | no |  |

#### Options for main > netobserv_flow_config_output_opensearch

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable output to OpenSearch. | bool | no | `False` |
| ecs_enable | Enable Elastic Common Schema. | bool | no | `False` |
| batch_deadline | Deadline for batch processing in milliseconds. | int | no | `2000` |
| batch_max_bytes | Maximum batch size in bytes. | int | no | `8388608` |
| timestamp_source | Source for event timestamps. | str | no | `collect` |
| index_period | Index period (daily, etc.). | str | no | `daily` |
| index_suffix | Suffix for index names. | str | no |  |
| index_template_enable | Enable index template management. | bool | no | `True` |
| index_template_overwrite | Overwrite existing index templates. | bool | no | `False` |
| index_template_shards | Number of primary shards for index templates. | int | no | `3` |
| index_template_replicas | Number of replica shards for index templates. | int | no | `1` |
| index_template_refresh_interval | Index refresh interval. | str | no | `10s` |
| index_template_codec | Codec for index template. | str | no | `best_compression` |
| index_template_ism_policy | ISM policy name. | str | no | `elastiflow` |
| index_template_pipeline_default | Default ingest pipeline. | str | no | `_none` |
| index_template_pipeline_final | Final ingest pipeline. | str | no | `_none` |
| addresses | OpenSearch node addresses. | str | no | `127.0.0.1:9200` |
| username | Username for OpenSearch. | str | no | `admin` |
| password | Password for OpenSearch. | str | no | `admin` |
| aws | AWS credentials for OpenSearch. | dict of `aws` [options](#options-for-main--netobserv_flow_config_output_opensearch--aws) | no |  |
| tls | TLS configuration for OpenSearch output. | dict of `tls` [options](#options-for-main--netobserv_flow_config_output_opensearch--tls) | no |  |
| retry_enable | Enable retry on failure. | bool | no | `True` |
| retry_on_timeout_enable | Enable retry on timeout. | bool | no | `True` |
| max_retries | Maximum number of retries. | int | no | `3` |
| retry_backoff | Backoff time between retries (ms). | int | no | `1000` |
| storage_optimization_enable | Enable storage optimization. | bool | no | `True` |
| drop_fields | Fields to drop from output. | str | no |  |
| allowed_record_types | Allowed record types for OpenSearch output. | str | no | `as_path_hop,flow_option,flow,ifa_hop,telemetry,metric,log` |

#### Options for main > netobserv_flow_config_output_opensearch > aws

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| access_key | AWS access key. | str | no | `None` |
| secret_key | AWS secret key. | str | no | `None` |
| region | AWS region. | str | no | `None` |

#### Options for main > netobserv_flow_config_output_opensearch > tls

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| client_ca_cert_filepath | Path to client CA certificate. | str | no |  |
| client_cert_filepath | Path to client certificate. | str | no |  |
| client_key_filepath | Path to client key. | str | no |  |
| enable | Enable TLS. | bool | no | `False` |
| skip_verification | Skip certificate verification. | bool | no | `False` |
| ca_cert_filepath | Path to CA certificate. | str | no |  |

#### Options for main > netobserv_flow_config_input_flow

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| server_udp_ip | UDP server IP address. | str | no | `0.0.0.0` |
| server_udp_port | UDP server port. | int | no | `9995` |
| server_udp_read_buffer_max_size | UDP read buffer max size. | int | no | `33554432` |
| packet_stream_max_size | Packet stream max size. | int | no | `512` |

#### Options for main > netobserv_flow_config_input_aws_vpc_flow_log_firehose

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| http_enable | Enable HTTP input for AWS Firehose. | bool | no | `False` |
| http_port | HTTP port for AWS Firehose. | int | no | `443` |
| http_access_key | AWS access key for Firehose. | str | no |  |
| http_log_format | Log format for AWS Firehose. | str | no | `${version} ${account-id} ${interface-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${packets} ${bytes} ${start} ${end} ${action} ${log-status}` |

#### Options for main > netobserv_flow_config_input_aws_vpc_flow_log_s3

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable S3 input. | bool | no | `False` |
| bucket | S3 bucket name. | str | no |  |
| prefix | S3 prefix. | str | no | `AWSLogs` |
| pool_size | Pool size for S3 input. | int | no | `None` |
| tls | TLS configuration for S3 input. | dict of `tls` [options](#options-for-main--netobserv_flow_config_input_aws_vpc_flow_log_s3--tls) | no |  |
| firehose_s3_enable | Enable Firehose S3 input. | bool | no | `False` |
| firehose_s3_log_format | Log format for Firehose S3. | str | no | `${version} ${account-id} ${interface-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${packets} ${bytes} ${start} ${end} ${action} ${log-status}` |
| aws | AWS credentials for S3 input. | dict of `aws` [options](#options-for-main--netobserv_flow_config_input_aws_vpc_flow_log_s3--aws) | no |  |

#### Options for main > netobserv_flow_config_input_aws_vpc_flow_log_s3 > tls

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable TLS for S3 input. Differs from default for security reasons | bool | no | `True` |
| skip_verification | Skip TLS certificate verification. | bool | no | `False` |
| ca_cert_filepath | Path to CA certificate file. | str | no |  |
| min_version | Minimum TLS version. | str | no | `1.2` |

#### Options for main > netobserv_flow_config_input_aws_vpc_flow_log_s3 > aws

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| access_key | AWS access key. | str | no | `None` |
| secret_key | AWS secret key. | str | no | `None` |

#### Options for main > netobserv_flow_config_input_azure_flow_log_vnet

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable Azure VNET input. | bool | no | `False` |
| config_file_path | Path to Azure VNET config file. | str | no | `/etc/elastiflow/azure/flowlog_vnet.yml` |
| config_values | Inline Azure VNET configuration values. Example: ```yaml - tenantId: "App registration Directory ID"   clientId: "App registration Application ID"   clientSecret: "App registration client secret"   consumers:     - namespace: "Host name of the Event Hubs namespace"       name: "Name of the Event Hub"       consumerGroup: "$Default" ``` | list of `` | no | `[]` |

#### Options for main > netobserv_flow_config_input_benchmark

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable benchmark input. | bool | no | `False` |
| packet_filepath | Path to benchmark packet file. | str | no | `/etc/elastiflow/benchmark/flow/packets.txt` |

#### Options for main > netobserv_flow_dashboards

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| elasticsearch | ElasticSearch dashboard import configuration. See: https://www.elastiflow.com/docs/data_platforms/elastic/kibana | dict of `elasticsearch` [options](#options-for-main--netobserv_flow_dashboards--elasticsearch) | no |  |
| opensearch | OpenSearch dashboard import configuration. See: https://www.elastiflow.com/docs/data_platforms/opensearch/dashboards | dict of `opensearch` [options](#options-for-main--netobserv_flow_dashboards--opensearch) | no |  |

#### Options for main > netobserv_flow_dashboards > elasticsearch

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable ElasticSearch dashboard import. | bool | no | `False` |
| url | URL for Kibana dashboard. | str | no | `https://raw.githubusercontent.com/elastiflow/elastiflow_for_elasticsearch/master/kibana/flow/kibana-8.14.x-flow-codex.ndjson` |
| override | Override existing dashboards. | bool | no | `True` |
| kibana_url | Kibana server URL. | str | no | `http://127.0.0.1:5601` |
| tls | TLS configuration for dashboard import. | dict of `tls` [options](#options-for-main--netobserv_flow_dashboards--elasticsearch--tls) | no |  |

#### Options for main > netobserv_flow_dashboards > elasticsearch > tls

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| validate_certs | Validate TLS certificates. | bool | no | `False` |
| ca_path | Path to CA certificate. | str | no | `None` |
| client_cert | Path to client certificate. | str | no | `None` |
| client_key | Path to client key. | str | no | `None` |

#### Options for main > netobserv_flow_dashboards > opensearch

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| enable | Enable OpenSearch dashboard import. | bool | no | `False` |
| url | URL for OpenSearch dashboard. | str | no | `https://raw.githubusercontent.com/elastiflow/elastiflow_for_opensearch/main/dashboards/flow/dashboards-2.14.x-flow-codex.ndjson` |
| override | Override existing dashboards. | bool | no | `True` |
| dashboards_url | OpenSearch Dashboards URL. | str | no | `http://127.0.0.1:5601` |
| tls | TLS configuration for dashboard import. | dict of `tls` [options](#options-for-main--netobserv_flow_dashboards--opensearch--tls) | no |  |

#### Options for main > netobserv_flow_dashboards > opensearch > tls

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| validate_certs | Validate TLS certificates. | bool | no | `False` |
| ca_path | Path to CA certificate. | str | no | `None` |
| client_cert | Path to client certificate. | str | no | `None` |
| client_key | Path to client key. | str | no | `None` |

#### Options for main > netobserv_flow_kernel_parameters

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| tune_enabled | Enable kernel tuning. | bool | no | `True` |
| net.core.netdev_max_backlog | Maximum number of packets allowed to queue when the interface receives packets faster than the kernel can process them. | int | no | `4096` |
| net.core.rmem_default | Default receive buffer size for network sockets. | int | no | `262144` |
| net.core.rmem_max | Maximum receive buffer size for network sockets. | int | no | `None` |
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
