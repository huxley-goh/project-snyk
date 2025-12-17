# Use an official Python runtime as a base image
FROM python:3.14-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the rest of the application code into the container
COPY app.py .

#Define the command to run the application when the container starts
ENTRYPOINT ["python", "app.py"]
