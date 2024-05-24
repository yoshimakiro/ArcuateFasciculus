# Dockerfile for the entire platform
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ /app/src/

CMD ["python", "src/main.py"]
