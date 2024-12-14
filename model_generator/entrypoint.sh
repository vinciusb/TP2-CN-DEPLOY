#!/bin/bash

cd /tmp
mkdir -p ./data
rm /tmp/data/*
wget -P /tmp/data $REPO_URL
LATEST_TAG=$(wget -qO- https://api.github.com/repos/vinciusb/TP2-CN-DEPLOY/tags | jq 'sort_by(.name) | .[-1] | .name')
export LATEST_TAG
cd /tmp
python3 model_generator.py