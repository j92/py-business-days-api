############################################################
# Dockerfile to build Python Application Containers
# Based on Ubuntu 16.10
############################################################

# Set the base image to Ubuntu
FROM ubuntu:16.10

# File Author / Maintainer
MAINTAINER Joost van Driel

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential zsh

# install python and python tools
RUN apt-get install -y python3.6 python-dev python-distribute python-pip

# Clone a git repo
RUN git clone https://github.com/j92/py-business-days-api.git

# Tell pip to download my dependencies
RUN pip install -r /py-business-days-api/requirements.txt

# Expose ports
EXPOSE 80

# Set the default directory where CMD will execute
WORKDIR /py-business-days-api

# Set the default command to execute
# when creating a new container
# i.e. using CherryPy to serve the application
CMD python server.py