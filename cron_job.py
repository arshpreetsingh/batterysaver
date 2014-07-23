from apscheduler.scheduler import Scheduler

sched = Scheduler()
sched.start()
from run_script import battery_check

# Start the scheduler
sched = Scheduler()
sched.start()

#start the job

sched.add_cron_job(battery_check, month='6-8,11-12', day='3rd fri', hour='0-3')
