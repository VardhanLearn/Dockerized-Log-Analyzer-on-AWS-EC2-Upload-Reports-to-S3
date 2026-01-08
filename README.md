# Dockerized-Log-Analyzer-on-AWS-EC2-Upload-Reports-to-S3

📌 Project Overview

This project demonstrates a Dockerized batch-processing application deployed on an AWS EC2 instance.
The application analyzes log files, generates a summary report, and uploads the output to Amazon S3.

👉 No Flask, no UI, no ECS — pure backend DevOps workflow.

This project is ideal for:

DevOps / Cloud portfolios

Docker & AWS hands-on practice

CI/CD and automation demonstrations

🧰 Tech Stack

Docker

Python 3.10

AWS EC2 (Ubuntu)

Amazon S3

AWS IAM (Role-based access)

AWS CLI

Git

📂 Project Structure

docker-log-analyzer/
├── app/
│   ├── analyze_logs.py
│   └── sample.log
├── Dockerfile
├── requirements.txt
└── README.md

⚙️ Application Workflow

Read log file (sample.log)

Count log levels:

INFO

WARNING

ERROR

Generate report file (log_summary.txt)

Upload the report to an Amazon S3 bucket

🐍 Application Code (Logic)

The Python application:

Parses logs using collections.Counter

Generates a text summary

Uses boto3 to upload results to S3

📦 requirements.txt
boto3

🐳 Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["python", "analyze_logs.py"]

☁️ AWS Prerequisites
1️⃣ EC2 Instance

Ubuntu 22.04

Instance type: t2.micro / t3.micro

Port 22 open for SSH

2️⃣ IAM Role

Attach the following policy to the EC2 instance:

AmazonS3FullAccess


This avoids hardcoding AWS credentials inside Docker containers.

🔧 EC2 Setup
sudo apt update
sudo apt install docker.io awscli git -y
sudo systemctl start docker
sudo usermod -aG docker ubuntu
logout


Log back in after logout.

🚀 Deployment Steps
1️⃣ Clone the Repository
git clone https://github.com/your-username/docker-log-analyzer.git
cd docker-log-analyzer

2️⃣ Build Docker Image
docker build -t log-analyzer:v1 .

3️⃣ Run the Container
docker run --rm log-analyzer:v1

📤 Output

Report generated: log_summary.txt

Automatically uploaded to:
