FROM centos:7

RUN curl https://copr.fedorainfracloud.org/coprs/g/ansible-service-broker/ansible-service-broker-nightly/repo/epel-7/group_ansible-service-broker-ansible-service-broker-nightly-epel-7.repo -o /etc/yum.repos.d/asb.repo
RUN yum -y install epel-release centos-release-openshift-origin \
 && yum -y install apb-container-scripts sudo origin-clients \
 && yum clean all

WORKDIR /mnt

RUN echo "ALL ALL=NOPASSWD: ALL" > /etc/sudoers.d/usermod
RUN chmod 666 /etc/passwd

ENTRYPOINT ["apb-wrapper"]
CMD ["-h"]

LABEL RUN docker run --privileged --rm -v \${PWD}:/mnt -v \$HOME/.kube:/.kube -v /var/run/docker.sock:/var/run/docker.sock -u \${SUDO_UID} \${IMAGE}
