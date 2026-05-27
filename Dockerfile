FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN apt-get install -y screen

ARG GIT_TOKEN

RUN git clone https://ssinghjah:$GIT_TOKEN@github.com/AERPAW/PROPSIM-Connector.git /root/propsim-connector

RUN cd /root/propsim-connector && pip install .


WORKDIR /root/propsim-connector/pchem
CMD ["python3", "server.py"]


