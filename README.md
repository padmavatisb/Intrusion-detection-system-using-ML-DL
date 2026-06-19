# 🚀 Cross-Dataset Generalized Intrusion Detection System (CD-GIDS)

## 📖 Overview

The Cross-Dataset Generalized Intrusion Detection System (CD-GIDS) is an AI-powered cybersecurity solution designed to detect malicious network activities across diverse network environments. Traditional Intrusion Detection Systems (IDS) often struggle when deployed on datasets different from those used during training. This project addresses this challenge through cross-dataset learning, feature alignment, and ensemble Machine Learning (ML) and Deep Learning (DL) techniques.

The system analyzes network traffic using packet header and flow-based features, ensuring privacy-preserving intrusion detection without payload inspection.

---

## 🎯 Problem Statement

Most IDS models achieve high accuracy on a single dataset but fail to generalize across unseen environments due to distribution shifts in network traffic patterns. This project aims to build a robust IDS capable of maintaining strong detection performance across multiple heterogeneous datasets.

---

## ✨ Key Features

- Cross-dataset intrusion detection
- Real-time network traffic monitoring
- CORAL-based feature alignment
- Ensemble ML and DL architecture
- Privacy-preserving flow-based analysis
- Dockerized deployment
- Web-based monitoring dashboard
- Low-latency attack detection

---

## 🏗️ System Architecture

```text
Network Traffic
      │
      ▼
Packet Capture (Scapy)
      │
      ▼
Feature Extraction
      │
      ▼
Data Preprocessing
      │
      ▼
CORAL Feature Alignment
      │
      ▼
ML & DL Models
      │
      ▼
Stacking Ensemble
      │
      ▼
Attack Classification
      │
      ▼
Real-Time Dashboard
```

---

## 📂 Datasets Used

The model is trained and evaluated using multiple cybersecurity datasets:

- CIC-IDS2017
- CSE-CIC-IDS2018
- CICIoT2023
- CICIoMT2024
- IoT Intrusion Dataset

### Attack Categories

- Port Scanning
- TCP Flood
- UDP Flood
- ICMP Flood
- DNS Flood
- SYN Flood
- HTTP Flood
- SSH Brute Force
- XMAS Scan
- Normal Traffic

---

## 🤖 Models Implemented

### Machine Learning Models

- LightGBM
- XGBoost
- Random Forest

### Deep Learning Models

- Deep Neural Network (DNN)
- Transformer Network
- BiLSTM
- CNN-TFE
- DAFN Hybrid Model

### Ensemble Strategy

A stacking-based ensemble combines predictions from multiple models to improve robustness and generalization performance.

---

## 🛠️ Technology Stack

### Languages

- Python
- SQL

### Libraries & Frameworks

- TensorFlow
- Scikit-Learn
- LightGBM
- XGBoost
- Pandas
- NumPy
- Scapy
- Flask
- Flask-SocketIO

### Tools

- Docker
- GitHub
- Google Colab
- Linux

---

## 📊 Results

| Evaluation Type | Accuracy |
|----------------|-----------|
| Cross-Dataset Detection | 90.01% |
| Combined Dataset Detection | 99.85% |

### Performance Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Matthews Correlation Coefficient (MCC)
- AUROC

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/padmavatisb/Intrusion-detection-system-using-ML-DL.git
cd Intrusion-detection-system-using-ML-DL
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Train the Model

```bash
python train.py
```

### Run Intrusion Detection

```bash
python inference.py
```

### Launch Dashboard

```bash
python app.py
```

Open your browser and navigate to:

```text
http://localhost:5000
```

---

## 🐳 Docker Deployment

Build Docker Image:

```bash
docker build -t cd-gids .
```

Run Docker Container:

```bash
docker run --cap-add=NET_ADMIN --cap-add=NET_RAW -p 5000:5000 cd-gids
```

---

## 📈 Future Enhancements

- Explainable AI (XAI) Integration
- Federated Learning-based IDS
- Edge Deployment for IoT Devices
- Cloud Threat Intelligence Integration
- Adversarial Attack Defense Mechanisms

---

## 📸 Project Screenshots

Add screenshots of:

- Dashboard<img width="855" height="375" alt="image" src="https://github.com/user-attachments/assets/bbdb35ee-8070-4b9a-bdf7-2a2660f8c864" /> <img width="855" height="370" alt="image" src="https://github.com/user-attachments/assets/b639ab83-d4c3-4ce7-9b71-c64dd7ee18a8" />


- Real-Time Attack Detection<img width="940" height="297" alt="image" src="https://github.com/user-attachments/assets/e64845b8-f1d5-4433-9453-bb1f11817c20" />

- Model Performance Graphs <img width="1772" height="725" alt="image" src="https://github.com/user-attachments/assets/fb292b32-f57c-4a1c-8ea4-b040a9d8f8c4" />




## 📜 License

This project is developed for academic and research purposes.

---

## ⭐ Support

If you find this project useful, consider giving it a star ⭐ on GitHub.
