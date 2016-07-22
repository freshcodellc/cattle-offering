FROM python:3.4
ENV PYTHONUNBUFFERED 1
ENV TERM linux
ENV TERMINFO /etc/terminfo
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r misc/requirements-dev.txt
