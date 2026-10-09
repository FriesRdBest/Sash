FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose Streamlit and optional API ports
EXPOSE 8501 8000

# Default command: run Streamlit (override in docker-compose for API)
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
