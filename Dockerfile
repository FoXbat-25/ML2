# Use Python 3.12 Slim as the base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY . /app

# Update package lists and install dependencies
RUN apt-get update && apt-get install -y curl unzip google-cloud-sdk

# Install Python dependencies
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "app.py"]
