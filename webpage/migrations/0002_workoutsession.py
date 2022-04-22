# Generated by Django 4.0.3 on 2022-04-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at', models.DateTimeField(blank=True, help_text="When your workout will take place. If it's a regular activity, leave this field out and specify the regularity in the description.", null=True, verbose_name='Date and time')),
                ('need_to_take', models.TextField(blank=True, help_text='What people should take with them', max_length=500)),
                ('duration', models.PositiveIntegerField(verbose_name='Duration in minutes')),
                ('description', models.TextField(blank=True, help_text="All people need to now about this workout that hasn't been specified", max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]