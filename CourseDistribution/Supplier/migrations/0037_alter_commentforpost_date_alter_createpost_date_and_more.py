# Generated by Django 4.1.4 on 2023-01-19 12:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0036_alter_follow_unique_together_follow_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentforpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 19, 18, 20, 43, 635300)),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 19, 18, 20, 43, 631304)),
        ),
        migrations.RemoveField(
            model_name='follow',
            name='post',
        ),
        migrations.AddField(
            model_name='follow',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='Supplier.createpost'),
        ),
    ]
