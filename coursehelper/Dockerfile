# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /coursehelper

# Copy the current directory contents into the container at /coursehelper
COPY . /coursehelper

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run manage.py on container startup
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
