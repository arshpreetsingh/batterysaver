"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second intervals.
"""
from run_script import battery_check
from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler


def Run_job():
	if _platform == "linux" or _platform == "linux2": 
    		os.system("python run_script.py")


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(Run_job, 'interval', seconds=3)
    scheduler.start()
    print("Battery Check has Just Started (press ctrl+c to stop)")
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()  # Not strictly necessary if daemonic mode is enabled but should be done if possible

