# Generated by Django 4.2 on 2023-05-29 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 29, 22, 10, 13, 33395, tzinfo=datetime.timezone.utc), verbose_name='Publication Date'),
        ),
    ]
