# Generated by Django 4.1.4 on 2023-01-14 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0012_alter_createpost_date_remove_followerscount_follower_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 14, 14, 57, 26, 658281)),
        ),
        migrations.RemoveField(
            model_name='followerscount',
            name='follower',
        ),
        migrations.AddField(
            model_name='followerscount',
            name='follower',
            field=models.CharField(default='3:00', max_length=1000),
            preserve_default=False,
        ),
    ]
