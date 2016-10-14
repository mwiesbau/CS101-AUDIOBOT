FROM ubuntu:16.04
MAINTAINER Mathias Wiesbauer <mathias.wiesbauer@gmail.com>

# UPGRADE LINUX
RUN apt-get update
RUN apt-get -y full-upgrade

# INSTALL PREREQUISITES
RUN apt-get install -y python-pip python-dev python-virtualenv redis-server git

# INSTALL TIPBOARD
RUN git clone https://github.com/allegro/tipboard.git
WORKDIR /tipboard
RUN python setup.py install
RUN tipboard create_project audiobot

# TRANSFER SETTINGS FROM LOCAL FOLDER
#ADD ./settings-local.py /root/.tipboard/settings-local.py
#ADD ./layout_config.yaml /root/.tipboard/layout_config.yaml


# RUN TIPBOARD AND THE REDIS INSTANCE
CMD service redis-server start && tipboard runserver 0.0.0.0 7272

