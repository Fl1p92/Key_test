from django.db import models


class Request(models.Model):

    path = models.CharField('Path', max_length=190, db_index=True)
    method = models.CharField('Method', max_length=10)
    time = models.DateTimeField('Request time', db_index=True)
    user = models.CharField('User', max_length=100, db_index=True)
    execution_time = models.DurationField('Execution time')

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'
        ordering = ['-time']

    def __str__(self):
        return f"{self.time.strftime('%d.%m.%y %H:%M:%S %Z')} {self.method} {self.path}"


class LogLine(models.Model):

    CREATE = "create"
    EDIT = "edit"
    DELETE = "delete"

    LOGGING_TYPES = (
        (CREATE, "Create"),
        (EDIT, "Edit"),
        (DELETE, "Delete"),
    )

    logging_time = models.DateTimeField('Logging time', auto_now_add=True)
    logging_type = models.CharField('Logging type', max_length=6, choices=LOGGING_TYPES, db_index=True)
    logging_text = models.TextField('Logging text')

    class Meta:
        verbose_name = 'Log line'
        verbose_name_plural = 'Log lines'
        ordering = ['-logging_time']

    def __str__(self):
        return f"{self.logging_time.strftime('%d.%m.%y %H:%M:%S %Z')} " \
               f"-- [{self.get_logging_type_display()}] -- {self.logging_text}"
