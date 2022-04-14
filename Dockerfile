from python:3.7.10-slim

RUN mkdir /src
COPY hello.py requirements.txt /src

WORKDIR /src
RUN pip install --upgrade pip \
    pip install -r requirements.txt

EXPOSE 5000

CMD ddtrace-run -d gunicorn hello:app --bind=0.0.0.0 --logger-class=logging.GunicornLogger
