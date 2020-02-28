FROM python:3.7.3-stretch
ENV PYTHONUNBUFFERED 1
WORKDIR /web_api
COPY . /web_api
RUN pip install --upgrade pip && pip install -r requirements.txt