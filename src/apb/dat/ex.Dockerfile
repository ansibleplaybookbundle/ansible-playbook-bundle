FROM ansibleplaybookbundle/apb-base
# MAINTAINER {{ $MAINTAINER }}

LABEL "com.redhat.apb.version"="0.1.0"
LABEL "com.redhat.apb.spec"=\

ADD apb /opt/apb

RUN useradd -u 1001 -r -g 0 -M -b /opt/apb -s /sbin/nologin -c "apb user" apb
RUN chown -R 1001:0 /opt/apb
USER 1001
