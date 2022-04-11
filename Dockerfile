
FROM python:3-alpine

RUN pip --no-cache-dir install pip --upgrade

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

WORKDIR /opt/api

COPY . /opt/api/

EXPOSE 8080

CMD ["python", "run.py"]

