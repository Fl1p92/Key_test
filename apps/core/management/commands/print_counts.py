from django.apps import apps
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Prints all models and objects counts.'

    def handle(self, *args, **options):
        models_list = apps.get_models()
        self.stdout.write(self.style.SUCCESS('In the current project:'))
        for i, model in enumerate(models_list, start=1):
            objects_count = model._default_manager.count()
            self.stdout.write(f'{i}) {model.__name__} model has {objects_count} objects.')
