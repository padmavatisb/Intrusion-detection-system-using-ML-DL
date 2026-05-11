FROM python:3.11-slim

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies for scapy
RUN apt-get update && apt-get install -y \
    tcpdump \
    iproute2 \
    net-tools \
    libpcap-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /ids

# Copy project files
COPY inference.py .
COPY app.py .
COPY templates/ templates/
COPY static/ static/

# Install Python dependencies
RUN pip install --no-cache-dir \
    scapy \
    flask \
    flask-socketio \
    python-socketio \
    eventlet \
    requests

# Expose dashboard port
EXPOSE 5000

# Default command (run IDS)
CMD ["python", "inference.py"]

