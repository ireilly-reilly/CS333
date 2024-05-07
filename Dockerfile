# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /IsaacSQL

# Copy the current directory contents into the container at /app
COPY . /IsaacSQL

# # Set environment variables to enable terminal interaction
# ENV PYTHONUNBUFFERED=1
# ENV PYTHONDONTWRITEBYTECODE=1

# Define the command to run your application
CMD ["python3", "main.py"]
