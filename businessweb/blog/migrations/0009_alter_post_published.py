# Generated by Django 4.2 on 2023-05-26 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 26, 16, 38, 59, 84772, tzinfo=datetime.timezone.utc), verbose_name='Publication Date'),
        ),
    ]