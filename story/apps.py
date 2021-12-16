from django.apps import AppConfig


class StoryConfig(AppConfig):
    name = 'story'

    def ready(self):
        if True:
            from lendigo import cron_job
            cron_job.start()
