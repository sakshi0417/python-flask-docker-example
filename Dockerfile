 # Use Python 3.9 as the base image
FROM python:3.9 
# Set the working directory inside the container
WORKDIR /app  

# Copy dependencies from requirements.txt
COPY requirements.txt .  

# Install dependencies
RUN pip install -r requirements.txt  

# Copy all project files to the working directory
COPY . .  

# Run the Flask app on startup
CMD ["python", "app.py"]  


