FROM centos:centos7
MAINTAINER dante-signal31 (dante.signal31@gmail.com)
RUN set -e
RUN yum -y update
RUN yum install -y ruby-devel curl libyaml-devel which tar rpm-build rubygems git python-setuptools zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel epel-release
RUN yum -y install python34
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN /usr/bin/python3 get-pip.py
RUN yum groupinstall -y "Development Tools"
# Preload useful dependencies to compile python distributions.
RUN yum-builddep python27 python34 -y
RUN gem install fpm