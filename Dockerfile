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
# Install dependencies globally, regenrate Pipfile.lock if outdated
RUN pipenv install --system --deploy --ignore-pipfile


EXPOSE 5000

#CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "--reload", "wsgi:app" ]