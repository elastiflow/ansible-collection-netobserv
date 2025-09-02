# ElastiFlow NetObserv Ansible Collection

- [ElastiFlow NetObserv Ansible Collection](#elastiflow-netobserv-ansible-collection)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Usage](#usage)
  - [Configuration](#configuration)
  - [Documentation](#documentation)
  - [Contribution](#contribution)
  - [License](#license)
  - [Author](#author)

This repository provides an [Ansible](https://www.ansible.com/) collection for installing and configuring [ElastiFlow NetObserv Collectors](https://www.elastiflow.com/docs/flowcoll/introduction).
It enables automated deployment, configuration, and kernel tuning for NetObserv Collectors on supported Linux platforms.

## Features

- Automated installation of NetObserv Collectors
- Configuration management for collection, enrichment, and output
- Kernel tuning for optimal performance
- Dashboard provisioning for ElasticSearch and OpenSearch
- Example playbooks for quick start

## Requirements

- Ansible 2.15+
- Tested platforms: Ubuntu 24.04, EL 9.5 (Rocky, Alma, RHEL)
- Minimum target host specs: 16GB RAM, 4 vCPUs
- SSH access to target hosts

## Usage

Sample playbooks are provided in the [`examples`](examples) directory:

- [examples/netobserv_flow_es_simple](https://github.com/elastiflow/ansible-collection-netobserv/tree/main/examples/netobserv_flow_es_simple): Deploy NetObserv Flow with "simple" ElasticSearch <!-- markdownlint-disable MD013 -->
- [examples/netobserv_flow_os_simple](https://github.com/elastiflow/ansible-collection-netobserv/tree/main/examples/netobserv_flow_os_simple): Deploy NetObserv Flow with "simple" OpenSearch <!-- markdownlint-disable MD013 -->

Please see the `README.md` in the relevant example.

## Configuration

- NetObserv Flow configuration options are documented in [roles/netobserv_flow/README.md](https://github.com/elastiflow/ansible-collection-netobserv/blob/main/roles/netobserv_flow/README.md).  

## Documentation

- [ElastiFlow Documentation](https://www.elastiflow.com/docs)
- [NetObserv Configuration Reference](https://www.elastiflow.com/docs/flowcoll/introduction)

## Contribution

Please follow the [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) when making contribution, TLDR:

- `fix: ...` - creates patch version release
- `feat: ...` - creates minor version release
- `feat!: ...` - creates major version release
- `chore: ...`/`doc: ...` - Does not create a release

## License

Apache-2.0

## Author
