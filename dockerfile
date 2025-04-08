# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy dependencies first
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY code.py /app/

# Set environment variables
ENV FLASK_APP=code.py

# Expose port 8000 for access
EXPOSE 8000

# Run Flask app
CMD ["python", "/app/code.py"]
