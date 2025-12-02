#!/bin/bash

docker run -d \
  --name analyze-app \
  --restart unless-stopped \
  --network host \
  smart_kip_analyze_data