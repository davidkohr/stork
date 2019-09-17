FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENTRYPOINT ["entrypoint.sh"]

# App setup
ADD . /code
WORKDIR /code

# Requirements installation
RUN pip install -r requirements.txt
RUN pip install https://bitbucket.org/dbenamy/devcron/get/tip.tar.gz
#COPY ./entrypoint.sh /


ENV SRC_DIR=/src \
    DEST_DIR=/opt/stork/ 

COPY ./ /code
