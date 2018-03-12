FROM ubuntu:16.04
# Basic Meta data about the Image maintainers
MAINTAINER Daniel Aboyewa <lolubyte.it@gmail.com>

ENV TERM=xterm-256color

# Install Ansible
RUN apt-get update -qy && \
    apt-get install -qy software-properties-common && \
    apt-add-repository -y ppa:ansible/ansible && \
    apt-get update -qy && \ 
    apt-get install -qy ansible

# Add colume for Ansible Playbook

VOLUME /ansible
WORKDIR /ansible

#set default for entrypoint and command string
ENTRYPOINT ["ansible-playbook"]
CMD ["site.yml"]
