#!/bin/bash
set -e

echo "[1/6] Enabling APIs..."
gcloud services enable aiplatform.googleapis.com texttospeech.googleapis.com

echo "[2/6] Installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y ffmpeg
pip install -r requirements.txt --upgrade

echo "[3/6] Authenticating..."
gcloud auth application-default login

echo "[4/6] Setting project..."
export GOOGLE_CLOUD_PROJECT=$(gcloud config get-value project)
echo "GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT" > .env

echo "[5/6] Starting Web App..."
python app.py

