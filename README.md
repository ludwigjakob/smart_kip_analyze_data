# SmartKIP Data Analysis

Analysis service to determine optimal fan thresholds based on historical temperature data.

## Features
- Read 7-day temperature and fan control history from InfluxDB
- Bayesian algorithm to calculate optimal temperature threshold
- Flask API to trigger analysis and check last run status

## Start the app with Docker
```bash
./start.sh
```

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses
This project uses third-party libraries under the following licenses:
- numpy (BSD-3-Clause)
- pandas (BSD-3-Clause)
- influxdb-client (MIT)
- python-dotenv (BSD-3-Clause)
- scikit-optimize (BSD-3-Clause)
- flask (BSD-3-Clause)
- apscheduler (MIT)
- mysql-connector-python (GPL-2.0 with FOSS Exception)
