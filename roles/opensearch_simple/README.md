<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: elastiflow.netobserv.opensearch_simple
Version: 0.1.3

Ansible collection for ElastiFlow NetObserv roles and playbooks.


## Requirements

| Platform | Versions |
| -------- | -------- |
| EL | 8, 9 |
| Ubuntu | jammy, noble |

## Role Arguments


### Entrypoint: main

"simple" role to install OpenSearch using the modified docker-compose file from the official [Docker Compose doc](https://docs.opensearch.org/docs/latest/install-and-configure/install-opensearch/docker/#sample-docker-composeyml)


|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| opensearch_version | OpenSearch version | str | no | `3.2.0` |
| opensearch_jvm_heap_size | JVM heap size | str | no | `5g` |
| opensearch_mem_limit | OpenSearch container memory limit. Should be roughly twice of the jvm_heap_size | str | no | `10g` |
| opensearch_initial_password | OpenSearch initial password for the default admin `elastic` user | str | no | `Strong1pass!` |



## Dependencies
None.

## Example Playbook

```
- hosts: all
  tasks:
    - name: Importing role: elastiflow.netobserv.opensearch_simple
      ansible.builtin.import_role:
        name: elastiflow.netobserv.opensearch_simple
      vars:
```

## License

Apache-2.0

## Author and Project Information
ElastiFlow Engineering Team <engineering@elastiflow.com>

<!-- END_ANSIBLE_DOCS -->
