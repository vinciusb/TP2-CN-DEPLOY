#!/bin/bash

cd /tmp
mkdir -p ./data
rm /tmp/data/*
wget -P /tmp/data $REPO_URL
LATEST_TAG=$(git describe --abbrev=0 --tags)
export LATEST_TAG
cd /tmp
python3 model_generator.py