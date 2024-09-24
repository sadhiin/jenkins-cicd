FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app/

RUN chmod +x /app/

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r src/requirements.txt

EXPOSE 8888

WORKDIR /app/src

# Set PYTHONPATH without using an undefined variable
ENV PYTHONPATH="/app/src"

# Install the package in editable mode
CMD ["pip", "install", "-e", "."]
