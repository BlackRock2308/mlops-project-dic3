# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ...
ENV APP_VERSION "1.0" 
# ...

# Set the working directory within the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the src directory into the container at /app/src
COPY src /app/src

# Copy the models directory into the container at /app/models
COPY models /app/models

# Copy the settings.py file into the container at /app
COPY settings /app/settings

# Expose the port that Flask app runs on
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=src/api.py

# Run the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
