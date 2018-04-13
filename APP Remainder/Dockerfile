FROM ubuntu
RUN apt-get update
COPY . /APP
RUN apt-get install -y python
ENTRYPOINT [ "python" "/APP/APPRemainder.py"]

