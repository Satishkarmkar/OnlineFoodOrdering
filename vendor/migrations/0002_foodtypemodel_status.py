# Generated by Django 3.0.2 on 2020-10-06 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtypemodel',
            name='status',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
