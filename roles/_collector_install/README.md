<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: elastiflow.netobserv._collector_install
Version: 0.3.1

Meta role for Elastiflow packages installation


## Requirements

| Platform | Versions |
| -------- | -------- |
| EL | 8, 9 |
| Ubuntu | jammy, noble |

## Role Arguments


### Entrypoint: main

Meta role for Elastiflow packages installation


|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| collector_type | Elastiflow package to install | str | no |  |
| version | Elastiflow package version | str | no |  |



## Dependencies
None.

## Example Playbook

```
- hosts: all
  tasks:
    - name: Importing role: elastiflow.netobserv._collector_install
      ansible.builtin.import_role:
        name: elastiflow.netobserv._collector_install
      vars:
```

## License

Apache-2.0

## Author and Project Information
ElastiFlow Engineering Team <engineering@elastiflow.com>

<!-- END_ANSIBLE_DOCS -->
