from django.db import models

from commons.utils import days_range

class JobManager(models.Manager):
    def filter_date(self):
        return super(JobManager, self).get_query_set().filter(posted__gt=days_range(30)) #TODO: make days range as config?