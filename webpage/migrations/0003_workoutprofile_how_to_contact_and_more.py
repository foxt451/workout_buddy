# Generated by Django 4.0.4 on 2022-05-06 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_workoutsession_how_to_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutprofile',
            name='how_to_contact',
            field=models.TextField(blank=True, help_text='How people can get in touch with you. This info will only be showed to authorized users.', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='workoutsession',
            name='how_to_contact',
            field=models.TextField(blank=True, help_text='How people can get in touch with you. This info will only be showed to authorized users.', max_length=300, null=True),
        ),
    ]
