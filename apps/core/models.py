from django.db import models


class Request(models.Model):

    path = models.CharField('Path', max_length=190, db_index=True)
    method = models.CharField('Method', max_length=10)
    time = models.DateTimeField('Request time', db_index=True)
    user = models.CharField('User', max_length=100, db_index=True)
    execution_time = models.DurationField('Execution time')

    def __str__(self):
        return f"{self.time.strftime('%d.%m.%y %H:%M:%S %Z')} {self.method} {self.path}"

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'
        ordering = ['-time']
