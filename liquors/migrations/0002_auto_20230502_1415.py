# Generated by Django 3.1.3 on 2023-05-02 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liquors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquor',
            name='url',
            field=models.URLField(default='www.google.com', max_length=300),
        ),
        migrations.AlterField(
            model_name='liquor',
            name='caducidad',
            field=models.DateField(default=datetime.datetime(2023, 8, 2, 14, 15, 54, 278394)),
        ),
    ]
