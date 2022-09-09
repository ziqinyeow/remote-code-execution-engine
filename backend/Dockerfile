FROM ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && apt-get install -y python3 python3-pip nodejs npm golang-go gcc mono-mcs openjdk-11-jre-headless && \
        rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY app.py .

ENTRYPOINT ["python3", "app.py"]