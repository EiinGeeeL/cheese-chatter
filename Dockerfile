FROM python:3.12.5-slim

RUN apt update -y
WORKDIR /app

COPY . /app
RUN python3 -m pip install -e .

# Expose the necessary port
EXPOSE 8000

# Set default command to run the app
CMD ["langgraph", "dev", "--port", "8000", "--host", "0.0.0.0"]