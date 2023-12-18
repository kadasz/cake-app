FROM python:3.11-slim

WORKDIR /app

COPY ./app /app/

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

CMD [ "python3", "/app/app.py" ]
