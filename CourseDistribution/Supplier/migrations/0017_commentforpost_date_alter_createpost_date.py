# Generated by Django 4.1.4 on 2023-01-17 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0016_createpost_insightful_alter_createpost_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentforpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 17, 12, 56, 49, 944165)),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 17, 12, 56, 49, 940168)),
        ),
    ]