from django.apps import apps
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Prints all models and objects counts.'

    def handle(self, *args, **options):
        models_list = apps.get_models()
        self.stdout.write(self.style.SUCCESS('In the current project:'))
        for index, model in enumerate(models_list, start=1):
            objects_count = model.objects.count()
            self.stdout.write(
                f'{index}) {model._meta.app_label}.{model._meta.model_name} has {objects_count} objects.'
            )
