# Generated by Django 2.2 on 2019-04-24 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(db_index=True, max_length=190, verbose_name='Path')),
                ('method', models.CharField(max_length=10, verbose_name='Method')),
                ('time', models.DateTimeField(db_index=True, verbose_name='Request time')),
                ('user', models.CharField(db_index=True, max_length=100, verbose_name='User')),
                ('execution_time', models.DurationField(verbose_name='Execution time')),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
                'ordering': ['-time'],
            },
        ),
    ]
