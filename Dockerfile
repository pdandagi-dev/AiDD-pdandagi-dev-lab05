# Step 1: Use an official Python runtime as a base image
FROM python:3.9-slim

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the rest of the application code
COPY . .

# Step 5: Expose the Flask port
EXPOSE 5000

# Step 6: Define environment variable
ENV FLASK_APP=app.py

# Step 7: Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
