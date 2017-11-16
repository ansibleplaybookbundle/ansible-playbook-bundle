# Ansible Playbook Bundle (APB)

An **Ansible Playbook Bundle (APB)** is a lightweight application definition (meta-container). They are used to define and deploy complex groups of applications, deployment configs, deployments, and services to an [OpenShift Origin](https://github.com/OpenShift/origin) cluster running the [Ansible Service Broker](https://github.com/openshift/ansible-service-broker).  APBs offer more power and simple configuration by leveraging the power of [Ansible](https://www.ansible.com/). APBs have the following features:

* Metadata contains list of required/optional parameters for use during deployment.
* Leverages existing investment in Ansible Roles / Playbooks.
* Actions under a directory with named  **_playbooks_** and metadata defined in **_apb.yml_**.
* Developer tooling to drive a guided approach.
* Easily modified or extended.

## Documentation
* [Getting Started](docs/getting_started.md) - step by step tutorial to create an Ansible Playbook Bundle
* [Design](docs/design.md) - overall design of Ansible Playbook Bundles
* [Developers](docs/developers.md) - in-depth explanation of Ansible Playbook Bundles
* [APB CLI Tool](docs/apb_cli.md) - installation and usage of the `apb` cli tool
* [Ansible Service Broker](https://github.com/openshift/ansible-service-broker) - more information about the Ansible Service Broker which runs APBs

