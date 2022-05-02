FROM ubuntu:latest
COPY ./requirements.txt /app2/requirements.txt

WORKDIR /app2
RUN yes | apt-get update -y
RUN yes | apt-get install python3-pip -y
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt

COPY . /app2

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]

