FROM python:3.10-slim

WORKDIR /ids

# System dependencies
RUN apt-get update && apt-get install -y \
    libgomp1 \
    tcpdump \
    iproute2 \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY models/ models/
COPY app/ app/
COPY logs/ logs/

# Python dependencies (IDS stack)
RUN pip install --no-cache-dir \
    numpy \
    pandas \
    joblib \
    scikit-learn \
    xgboost \
    lightgbm \
    scapy

CMD ["python", "app/inference.py"]

