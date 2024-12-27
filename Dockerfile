FROM python:3.12.5-slim

RUN apt update -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

# Expose the necessary port
EXPOSE 8000

# Set default command to run the app
CMD ["langgraph", "dev", "--port", "8000", "--host", "0.0.0.0"]