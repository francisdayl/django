FROM python

RUN apt-get update \
 && apt-get install wget

RUN pip3 install numpy django pillow 


WORKDIR /work