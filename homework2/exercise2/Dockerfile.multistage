# Stage 1 - Build Stage:
# Use python:3.11 
FROM python:3.11 AS stage1

# Set working directory to /app
WORKDIR /app

# Install build dependencies 
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
  && rm -rf /var/lib/apt/lists/*

# Copy requirements file and run pip install
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

# Stage 2 - Runtime Stage:
# Use python:3.11-alpine (minimal Alpine-based Python image)
FROM python:3.11-alpine AS stage2

# Set working directory to /app
WORKDIR /app

# Copy the installed packages from the build stage
COPY --from=stage1 /install /usr/local

# Copy application code
COPY . .

#Expose port 5000
EXPOSE 5000

#Set the startup command
CMD ["python", "-m", "app"]