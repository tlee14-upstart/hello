from python:3.7.10-slim

RUN mkdir /src
COPY hello.py requirements.txt /src

WORKDIR /src
RUN pip install --upgrade pip \
    pip install -r requirements.txt

EXPOSE 5001
ENV FLASK_APP=hello

CMD flask run --host=0.0.0.0 --port 5001
