# Generated by Django 3.1.5 on 2021-01-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20210121_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='rate',
            field=models.FloatField(default=0),
        ),
    ]
