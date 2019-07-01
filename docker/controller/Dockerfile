FROM python:3.7.3-stretch
ENV PYTHONUNBUFFERED 1
WORKDIR /src
COPY . /src
RUN pip install --upgrade pip && pip install -r requirements.txt