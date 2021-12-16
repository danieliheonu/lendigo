from apscheduler.schedulers.background import BackgroundScheduler
from story.views import new_story

def start():
    scheduler = BackgroundScheduler()

    @scheduler.scheduled_job('interval', minutes=5, name='job')
    def job():
        new_story()

    scheduler.start()