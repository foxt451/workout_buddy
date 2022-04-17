# Generated by Django 4.0.3 on 2022-04-16 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_workoutsession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutsession',
            name='at',
            field=models.DateField(blank=True, help_text="When your workout will take place. If it's a regular activity, leave this field empty and specify the regularity in the description.", null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='workoutsession',
            name='description',
            field=models.TextField(blank=True, help_text="All people need to now about this workout that hasn't yet been specified (like specific time or prerequisits...)", max_length=2000),
        ),
    ]
