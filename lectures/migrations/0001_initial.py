# Generated by Django 3.0.6 on 2020-06-25 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LectureVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('disc', models.TextField()),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Topics',
            },
        ),
    ]
