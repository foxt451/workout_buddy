# Generated by Django 4.0.3 on 2022-04-17 03:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0006_alter_workoutsession_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutsession',
            name='name',
            field=models.CharField(default='Kek', help_text='Give it a name', max_length=255, validators=[django.core.validators.MinLengthValidator(3)]),
            preserve_default=False,
        ),
    ]