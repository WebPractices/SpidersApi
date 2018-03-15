from apscheduler.schedulers.blocking import BlockingScheduler

from spiders.bing_paper import main


scheduler = BlockingScheduler()
scheduler.add_job(main, 'cron', day_of_week='0-6', hour=6, minute=30)
scheduler.start()
