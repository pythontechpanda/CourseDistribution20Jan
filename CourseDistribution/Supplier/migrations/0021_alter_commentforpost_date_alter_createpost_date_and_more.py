# Generated by Django 4.1.4 on 2023-01-18 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0020_alter_commentforpost_date_alter_createpost_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentforpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 18, 11, 6, 29, 724589)),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 18, 11, 6, 29, 720593)),
        ),
        migrations.AlterField(
            model_name='followerscount',
            name='user',
            field=models.CharField(max_length=1000),
        ),
    ]
