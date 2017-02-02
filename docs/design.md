# AnsibleApp Spec File

Example:

```yaml
---
ansibleapps:
  - id: c9e3348c-b6fd-45d6-b2ba-a13b41f0b6e3
    name: fusor/etherpad-ansibleapp
    description: Note taking web application
    bindable: true
    async: optional
    parameters:
      - name: hostport
        description: The host TCP port as the external endpoint
        type: int
        default: 9001
      - name: db_user
        description: Database User
        type: string
      - name: db_pass
        description: Database Password
        type: string
      - name: db_name
        description: Database Name
        type: string
      - name: db_host
        description: Database service hostname/ip
        default: mariadb
        type: string
      - name: db_port
        description: Database service port
        type: int
        default: 3306
```

> TODO: Explain specfile base64 encoding and label stamp

## Specifying Configuration Parameters

`parameters` section of the specfile; `ParameterObject` array

**ParameterObject**

Field Name | Description
---|---
name | **Required.** The name of the parameter.
description | **Required.** A human readable description of the parameter.
type | **Required** Type of parameter. `bool`, `int`, `float`, `string`, are valid
default | **Optional** An optional default value for the parameter.

> TODO: Lack of default signifies a required answer?

## Running AnsibleApps

AnsibleApps are containers that are run with the following command:

`docker run $container_name $action $arguments`

* `container_name`

The name of the ansibleapp container, i.e. `ansibleapp/etherpad`

* `action`

One of the 4 possible actions an ansible app can take. At a minimum, an ansibleapp
must implement provision and deprovision.

```
* provisoin
* deprovision
* bind
* unbind
```

* `arguments`

Arguments in the form of a JSON payload that an ansibleapp may need to perform
a specified action. JSON is an `Arguments` object:

**Arguments**

Field Name | Description
---|---
instance_id | **Required** Service instance id. UUID string
answers | **Required.** JSON object containing key-value answers for parameter config
cluster | **Required.** `ClusterObject` containing targetted cluster information and credentials (TBD)

> TODO: ## Authentication section to better describe ClusterObject schema and what's included

> TODO: ## Dependencies! How is the container graph represented in a spec file. Is it necessary?
