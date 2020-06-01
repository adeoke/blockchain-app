FROM python:3.6-alpine


RUN mkdir /blockchainapp

#change to the djangoapi dir
WORKDIR /djangoapi

#copy all content from host directory to image directory.
COPY . /blockchainapp/

# Set environment variables
ENV PYTHONUNBUFFERED 1

# execute immediately
RUN apk update \
    && apk add openssh-server \
    && apk add --virtual build-deps gcc musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip3 install pipenv \
    && pipenv install -r requirements.txt --deploy --ignore-pipfile \
    && apk del build-deps
