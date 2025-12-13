# SmartKIP Data Analysis

Analysis service to determine optimal fan thresholds based on historical temperature data.

## Features
- Read 7-day temperature and fan control history from InfluxDB
- Bayesian algorithm to calculate optimal temperature threshold
- Flask API to trigger analysis and check last run status

## Start the app with Docker
```bash
./start.sh
