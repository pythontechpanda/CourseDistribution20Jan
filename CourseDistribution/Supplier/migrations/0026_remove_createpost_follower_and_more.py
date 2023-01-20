# Generated by Django 4.1.4 on 2023-01-18 07:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Supplier', '0025_createpost_follower_alter_commentforpost_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createpost',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='followerscount',
            name='post',
        ),
        migrations.RemoveField(
            model_name='followerscount',
            name='user',
        ),
        migrations.RemoveField(
            model_name='followerscount',
            name='value',
        ),
        migrations.AddField(
            model_name='followerscount',
            name='following_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followerscount',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='commentforpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 18, 12, 32, 28, 900689)),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 18, 12, 32, 28, 896693)),
        ),
    ]