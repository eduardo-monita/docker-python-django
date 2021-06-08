FROM python:3.8-slim
    
# Ajusting TimeZone
ENV TZ=America/Sao_Paulo
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
RUN echo "America/Sao_Paulo" > /etc/timezone

# set work directory
WORKDIR /app

RUN apt-get update && apt-get -y upgrade && apt-get install -y build-essential gettext

COPY ./app/requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install gunicorn Django==3.1.*
RUN pip install -r requirements.txt

COPY ./app /app/
