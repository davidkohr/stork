FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENTRYPOINT ["entrypoint.sh"]

EXPOSE 8080
RUN pip install https://bitbucket.org/dbenamy/devcron/get/tip.tar.gz

COPY ./requirements.txt /code/
WORKDIR /code
# Requirements installation
RUN pip install -r /code/requirements.txt
RUN pip install psycopg2-binary
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
# App setup
COPY ./ /code
COPY entrypoint.sh /bin/entrypoint.sh

RUN chmod +x /bin/entrypoint.sh
