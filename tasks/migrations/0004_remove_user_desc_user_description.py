# Generated by Django 4.1.2 on 2023-02-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_user_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='desc',
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
