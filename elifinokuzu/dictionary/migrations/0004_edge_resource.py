# Generated by Django 2.0.1 on 2018-07-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_auto_20180722_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='edge',
            name='resource',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
