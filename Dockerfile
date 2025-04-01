# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install -r requirements.txt

# Expose the port that Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
