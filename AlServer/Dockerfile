# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
FROM tensorflow/tensorflow

WORKDIR /python-docker

COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /python-docker

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]