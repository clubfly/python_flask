FROM ubuntu:16.04
RUN sed -i'' 's/archive\.ubuntu\.com/tw\.archive\.ubuntu\.com/' /etc/apt/sources.list
RUN apt-get update -y && apt-get clean
RUN apt-get install -y cron vim python3-pip python3-dev openssl libssl-dev locales tzdata
COPY . /opt/vcms
WORKDIR /opt/vcms
RUN pip3 install --upgrade pip
RUN pip install -r setup/requirements.txt
ADD crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab
RUN sed -i '/session    required     pam_loginuid.so/c\#session    required   pam_loginuid.so' /etc/pam.d/cron
RUN ln -fs /usr/share/zoneinfo/Asia/Taipei /etc/localtime
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV PYTHONIOENCODING=utf-8
ENV DEBIAN_FRONTEND=noninteractive
