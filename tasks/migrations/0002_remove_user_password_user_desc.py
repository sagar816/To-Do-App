# Generated by Django 4.1.2 on 2023-02-24 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='desc',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]