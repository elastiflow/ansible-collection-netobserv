# NetObserv Flow with ElasticSearch

- [NetObserv Flow with ElasticSearch](#netobserv-flow-with-elasticsearch)
  - [Overview](#overview)
  - [Run the playbook](#run-the-playbook)

## Overview

This playbook deploys NetObserv Flow with ElasticSearch as the data platform.  
Intended for demonstration, testing, or proof-of-concept use only.

**Requirements:**

- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) must be installed:
  - Mac
  
    ```sh
    brew install ansible
    ```

- Target host: Ubuntu 24.04/Rocky 9, minimum 16GB RAM and 4 vCPUs.  
  For larger systems, increase ElasticSearch memory allocation:
  
  ```yaml
  ElasticSearch_jvm_heap_size: "5g"
  ElasticSearch_mem_limit: "9g" # Should be about twice ElasticSearch_jvm_heap_size
  ```
  
- SSH authentication to the target host via SSH key is required.

## Run the playbook

- Clone this repository and navigate to the directory, or copy `playbook.yml`, `requirements.yml`, and `ansible.cfg`.
- Install Ansible requirements:
  
  ```sh
  ansible-galaxy install -r requirements.yml
  ```

- Run the playbook:
  
  ```sh
  ansible-playbook -i '${HOST_IP},' -u ${SUDO_SSH_USER} playbook.yml

  # Example
  ansible-playbook -i '10.100.3.63,' -u elastiflow playbook.yml
  ```

- Access ElasticSearch Dashboards at `http://${HOST_IP}:5601` (user: `elastic`, password: `Elast1flow!`). Use the "Global" tenant.
- After the playbook completes, dashboards will be available in ElasticSearch Dashboards at the same address.
