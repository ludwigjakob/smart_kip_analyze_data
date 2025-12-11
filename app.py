from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess, datetime

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()

last_run = None

def run_analysis():
    global last_run
    subprocess.run(["python", "main.py"])
    last_run = datetime.datetime.now(datetime.UTC)

@app.route("/run", methods=["POST"])
def run_manual():
    run_analysis()
    return jsonify({"status": "started"})

@app.route("/status")
def status():
    return jsonify({"last_run": last_run})

# Scheduler automatisch alle 2 Tage
# scheduler.add_job(run_analysis, "interval", days=2)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)