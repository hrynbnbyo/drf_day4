# Generated by Django 2.0.6 on 2021-04-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
