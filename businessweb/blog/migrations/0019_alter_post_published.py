# Generated by Django 4.2 on 2023-05-26 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 26, 17, 4, 14, 189488, tzinfo=datetime.timezone.utc), verbose_name='Publication Date'),
        ),
    ]
