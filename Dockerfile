FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY tarot_app.py .
COPY templates/ templates/
COPY static/ static/

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "tarot_app.py"]
