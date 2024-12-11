#!/bin/bash

cd /tmp
mkdir -p ./data
rm /tmp/data/*
wget -P /tmp/data $REPO_URL
cd /tmp
python3 model_generator.py