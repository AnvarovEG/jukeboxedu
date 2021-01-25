# Generated by Django 3.1.5 on 2021-01-21 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='albums', to='music.artist'),
        ),
        migrations.AlterField(
            model_name='track',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tracks', to='music.artist'),
        ),
    ]
