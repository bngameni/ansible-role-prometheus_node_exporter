# Ansible role - prometheus_node_exporter
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-prometheus_node_exporter?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-prometheus_node_exporter?style=flat-square)](https://github.com/claranet/ansible-role-prometheus_node_exporter/releases)
[![Status](https://img.shields.io/github/workflow/status/claranet/ansible-role-prometheus_node_exporter/Ansible%20Molecule?style=flat-square&label=tests)](https://github.com/claranet/ansible-role-prometheus_node_exporter/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/prometheus_node_exporter)


> :star: Star us on GitHub — it motivates us a lot!

Install and configure Prometheus Node Exporter

## :warning: Requirements

Ansible >= 2.10

## :zap: Installation

```bash
ansible-galaxy install claranet.prometheus_node_exporter
```

## :gear: Role variables

Variable | Default value | Description
---------|---------------|------------
prometheus_node_exporter_version     | **1.4.0**      | Version of node exporter to install   
prometheus_node_exporter_service_enabled     | **true**      | Enable prometheus node exporter service 

## :arrows_counterclockwise: Dependencies

N/A

## :pencil2: Example Playbook

```yaml
---
- hosts: all
  roles:
    - claranet.prometheus_node_exporter
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
