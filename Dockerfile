# Set Python version
FROM python:3.12.9

# Set working directory
WORKDIR /app

# Add requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Add app files
COPY . .

# Run the app
CMD ["python", "app.py"]
