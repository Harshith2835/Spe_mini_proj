# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set maintainer information
LABEL maintainer="Harshith"
LABEL description="Scientific Calculator Application with DevOps Pipeline"
LABEL version="1.0.0"

# Set working directory inside container
WORKDIR /app

# Create a non-root user for security
RUN groupadd -r calcuser && useradd -r -g calcuser calcuser

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY calculator.py .
COPY test_calculator.py .

# Create logs directory and set permissions
RUN mkdir -p /app/logs && chown -R calcuser:calcuser /app

# Switch to non-root user
USER calcuser

# Expose port (if needed for future web interface)
EXPOSE 8080

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "from calculator import ScientificCalculator; calc = ScientificCalculator(); print('Health check passed')" || exit 1

# Default command to run the calculator
CMD ["python3", "calculator.py"]