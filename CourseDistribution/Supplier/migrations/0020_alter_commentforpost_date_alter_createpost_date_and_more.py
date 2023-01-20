# Generated by Django 4.1.4 on 2023-01-18 05:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Supplier', '0019_followerscount_alter_commentforpost_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentforpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 18, 10, 37, 27, 838621)),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 18, 10, 37, 27, 832627)),
        ),
        migrations.AlterField(
            model_name='followerscount',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='followerscount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]