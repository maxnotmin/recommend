# Generated by Django 3.0.6 on 2020-05-19 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='summary',
            field=models.TextField(default='Summary Default'),
        ),
    ]
