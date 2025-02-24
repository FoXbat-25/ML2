FROM python:3.12-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y&&apt  -y curl unzip

# Install Google Cloud SDK (includes gsutil for GCP storage)
RUN curl https://sdk.cloud.google.com | bash && \
    exec -l $SHELL && \
    gcloud auth login
RUN apt-get update && pip install -r requirements.txt
CMD ['python', 'app.py']
