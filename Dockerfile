FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /testing
WORKDIR /testing
ADD . /testing/
RUN pip install -r requirements.txt