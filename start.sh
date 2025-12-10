#!/bin/bash

# Image neu bauen
docker build -t smart_kip_analyze_data .

docker run -d \
  --name analyze-app \
  --restart unless-stopped \
  --network host \
  smart_kip_analyze_data