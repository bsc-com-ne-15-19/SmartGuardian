FROM python:3.12.2-alpine

# Install PostgreSQL development package
# RUN apk add --no-cache postgresql-dev
ENV MAPBOX_API_KEY pk.eyJ1IjoiYXVicmV5bXV3YWxvIiwiYSI6ImNsdGIxZjVvcTFtdmUybW1zcG9jeHFmYmIifQ.hAa-71IJ_PvPa3S981-syw

ENV MQTT_BROKER_ADDRESS 20d34d0715dc40bd94844427c77b2dd5.s1.eu.hivemq.cloud
ENV MQTT_USERNAME SmartGuardian
ENV MQTT_PASSWORD BSC-COM-NE-15-19@unima.ac.mw

# install psycopg2 dependencies
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

# Set work directory
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYCODE 1

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
# Install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# Copy source code
COPY . /usr/src/app/
# Run the application

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
