# Use official Python image as base
FROM python:3.12

# Set working directory to /app
WORKDIR /app

# Copy requirements file and run pip install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

#Expose port 5000
EXPOSE 5000

#Set the startup command
CMD ["python", "-m", "app"]