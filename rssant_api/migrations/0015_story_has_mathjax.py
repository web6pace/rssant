# Generated by Django 2.2.6 on 2019-10-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rssant_api', '0014_auto_20191027_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='has_mathjax',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
