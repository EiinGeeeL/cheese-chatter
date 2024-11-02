FROM python:3.12.5-slim

RUN apt update -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]