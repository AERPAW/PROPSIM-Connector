FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN apt-get install -y screen

ARG GIT_TOKEN=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

RUN git clone https://ssingh28:$GIT_TOKEN@github.ncsu.edu/AERPAW/PROPSIM-Connector.git /root/propsim-connector

RUN cd /root/propsim-connector && pip install .

CMD cd /root/propsim-connector && screen -S pchem-server -dm bash -c 'stdbuf -oL -eL python3 server.py'


