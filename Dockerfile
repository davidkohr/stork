FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENTRYPOINT ["entrypoint.sh"]

EXPOSE 8080

# App setup
COPY ./ /code
WORKDIR /code
COPY entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh

# Requirements installation
RUN pip install -r /code/requirements.txt
RUN pip install https://bitbucket.org/dbenamy/devcron/get/tip.tar.gz

ENV SRC_DIR=/src \
    DEST_DIR=/opt/stork/
