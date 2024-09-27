# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./activity1 /app

# Install any needed packages specified in activity1/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask to run in production
ENV FLASK_APP=app:app
ENV FLASK_ENV=production

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]

