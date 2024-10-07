# Example Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy your application files
COPY requirements.txt requirements.txt

# Upgrade pip and install requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

