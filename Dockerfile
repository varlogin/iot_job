FROM python:3.10

COPY requirements.txt /tmp/
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
