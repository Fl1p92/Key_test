from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.core.models import LogLine, Request
from apps.user_profile.models import Profile


@receiver(post_save, sender=Profile)
@receiver(post_save, sender=User)
def create_save_log_line(sender, instance, created, **kwargs):
    if created:
        log_type = LogLine.CREATE
        log_text = f'New {instance._meta.app_label}.{instance._meta.model_name} "{instance}" is created!'
    else:
        log_type = LogLine.EDIT
        log_text = f'{instance._meta.app_label}.{instance._meta.model_name} "{instance}" is edited!'
    LogLine.objects.create(logging_type=log_type, logging_text=log_text)


@receiver(post_delete, sender=Profile)
@receiver(post_delete, sender=Request)
@receiver(post_delete, sender=User)
def create_delete_log_line(sender, instance, **kwargs):
    log_type = LogLine.DELETE
    log_text = f'{instance._meta.app_label}.{instance._meta.model_name} "{instance}" is deleted!'
    LogLine.objects.create(logging_type=log_type, logging_text=log_text)
