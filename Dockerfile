# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files to the working directory
COPY main.py .
COPY spxing spxing
COPY requirements.txt .

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        libffi-dev \
        libssl-dev \
        libxml2-dev \
        libxslt1-dev \
        zlib1g-dev \
        git \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables (if needed)
# ENV VAR_NAME=value

# Expose any necessary ports (if needed)
# EXPOSE port_number

# Set the entry point command for the container
CMD ["python", "main.py"]
