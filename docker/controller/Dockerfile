FROM python:3.7.3-stretch
ENV PYTHONUNBUFFERED 1
WORKDIR /controller
COPY . /controller
RUN pip install --upgrade pip && pip install -r requirements.txt