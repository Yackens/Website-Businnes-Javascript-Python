# Generated by Django 4.2 on 2023-05-26 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 26, 16, 43, 11, 666797, tzinfo=datetime.timezone.utc), verbose_name='Publication Date'),
        ),
    ]
