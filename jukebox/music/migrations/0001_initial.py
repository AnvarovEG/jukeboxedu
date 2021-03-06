# Generated by Django 3.1.5 on 2021-01-21 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('start_year', models.IntegerField(default=2021)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('year', models.IntegerField(default=2021)),
                ('bpm', models.IntegerField(null=True)),
                ('is_ep', models.BooleanField(default=False)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='music.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField(default=2021)),
                ('title', models.CharField(max_length=128)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='music.artist')),
                ('tracks', models.ManyToManyField(to='music.Track')),
            ],
        ),
    ]
