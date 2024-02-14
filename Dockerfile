FROM python:3.11-slim

RUN mkdir -p /opt/app & \
    addgroup --gid 9999 app & \
    adduser --uid 9999 --gid 9999 --disabled-password --home /opt/app --gecos "Application user" app
RUN usermod -L app & chown -R app:app /opt/app

COPY --chown=app:app ./app /opt/app

USER app
WORKDIR /opt/app

RUN pip install --user --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

CMD [ "python3", "/opt/app/app.py" ]
