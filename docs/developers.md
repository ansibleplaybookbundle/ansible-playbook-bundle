# How to create an ansibleapp project

Directory layout of an ansibleapp
```
AnsibleApplication/
    Dockerfile
    ansibleapp/
        actions/
            provision.yaml
            deprovision.yaml
            bind.yaml
            unbind.yaml
```

These playbooks are called when their respective action is passed into the ansibleapp meta container.

Example Dockerfile
```
FROM ansibleapp/ansibleapp-base

MAINTAINER Dylan Murray <dymurray@redhat.com>

ADD ansibleapp/actions /ansibleapp/actions
```

This Dockerfile is based off ansibleapp/ansibleapp-base which has an entrypoint script which will call the respective playbook out of /ansibleapp/actions/ as well as handling authentication.

Running an Ansibleapp
```
docker run -e "OPENSHIFT_TARGET=<oc_cluster_address>" -e "OPENSHIFT_USER=<oc_user>" -e "OPENSHIFT_PASS=<oc_pass>" <ansibleapp_name> $action
ex: docker run -e "OPENSHIFT_TARGET=cap.example.com:8443" -e "OPENSHIFT_USER=admin" -e "OPENSHIFT_PASS=admin" ansibleapp/etherpad-ansibleapp provision
```
