FROM python:3.7.1-alpine
LABEL maintainer="Pierre-Henri Bourdeau <phbasic@gmail.com>"

RUN apk --no-cache add openssl-dev
RUN apk --no-cache add --virtual \
    build-dependencies \
    gcc \
    g++ \
    make \
    libffi-dev \
    libxslt-dev \
    py-gunicorn

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

#RUN pipenv run flask init_db
#RUN pipenv run flask db upgrade
#RUN pipenv run flask db migrate

EXPOSE 5000