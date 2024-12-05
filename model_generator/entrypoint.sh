#!/bin/bash

cd /tmp
mkdir -p ./data
wget -P /tmp/data https://raw.githubusercontent.com/vinciusb/TP2-CN-DATA/refs/heads/main/2023_spotify_ds1.csv
cd /tmp
python3 model_generator.py