FROM ubuntu
RUN apt-get update
COPY . /APP
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get install cron
RUN crontab /APP/user.cron