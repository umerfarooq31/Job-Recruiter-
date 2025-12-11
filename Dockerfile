# --- Dockerfile ---

# Use the official Python image as the base image (slim is recommended for smaller size)
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
# We use separate steps to leverage Docker's build cache
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire Django project code into the container
COPY . /app/

# Expose the port the application will run on
EXPOSE 8000

# Command to run the application using Gunicorn (recommended for production/container environments)
# If you don't have Gunicorn installed, you should add it to requirements.txt.
# Assuming Gunicorn is used, otherwise, use: CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# The project name is Job_Pro.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]