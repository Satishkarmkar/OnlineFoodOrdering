# Generated by Django 3.0.2 on 2020-09-05 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CuisineModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100, unique=True)),
                ('photo', models.ImageField(upload_to='cuisine_images/')),
            ],
        ),
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('photo', models.ImageField(upload_to='state_images/')),
            ],
        ),
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('photo', models.ImageField(upload_to='city_images/')),
                ('city_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pwn.StateModel', unique=True)),
            ],
        ),
    ]