<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: elastiflow.netobserv.elasticsearch_simple
Version: 0.1.4

Ansible collection for ElastiFlow NetObserv roles and playbooks.


## Requirements

| Platform | Versions |
| -------- | -------- |
| EL | 8, 9 |
| Ubuntu | jammy, noble |

## Role Arguments


### Entrypoint: main

"simple" role to install ElasticSearch using the modified docker-compose file from the official [Docker Compose doc](https://github.com/elastic/elasticsearch/blob/main/docs/reference/setup/install/docker/docker-compose.yml)


|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| elasticsearch_version | ElasticSearch version | str | no | `9.1.2` |
| elasticsearch_jvm_heap_size | JVM heap size | str | no | `5g` |
| elasticsearch_mem_limit | ElasticSearch container memory limit. Should be roughly twice of the jvm_heap_size | str | no | `10g` |
| elasticsearch_kibana_mem_limit | Kibana container memory limit | str | no | `1g` |
| elasticsearch_initial_password | ElasticSearch initial password for the default admin `elastic` user | str | no | `Strong1pass!` |



## Dependencies
None.

## Example Playbook

```
- hosts: all
  tasks:
    - name: Importing role: elastiflow.netobserv.elasticsearch_simple
      ansible.builtin.import_role:
        name: elastiflow.netobserv.elasticsearch_simple
      vars:
```

## License

Apache-2.0

## Author and Project Information
ElastiFlow Engineering Team <engineering@elastiflow.com>

<!-- END_ANSIBLE_DOCS -->
