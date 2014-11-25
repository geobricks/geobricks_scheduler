from apscheduler.schedulers.blocking import BlockingScheduler


scheduler = BlockingScheduler()

# Field 	    Description
# year 	        4-digit year number
# month 	    month number (1-12)
# day 	        day of the month (1-31)
# hour 	        hour (0-23)
# minute    	minute (0-59)

@scheduler.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every three minutes.')

@scheduler.scheduled_job('cron', day_of_week='mon', hour=9, minute=28)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

scheduler.start()