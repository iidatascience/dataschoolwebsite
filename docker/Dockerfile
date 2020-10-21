FROM alpine:latest
LABEL Maintainer="II Data School <info@iidatascience.com>"\
        Description="II Data Science - Website"

WORKDIR /var/www/html

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN apk --no-cache add git
RUN pip3 install psycopg2-binary

RUN git clone -b integration https://github.com/iidatascience/dataschoolwebsite.git && cd dataschoolwebsite

ADD sqlconfig.xml /var/www/html/dataschoolwebsite/tjgwebservices/views/static/xml/


CMD ["python", "/var/www/html/dataschoolwebsite/datascience.py"]

EXPOSE 8080
