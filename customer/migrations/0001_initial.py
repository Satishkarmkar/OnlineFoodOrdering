# Generated by Django 3.0.2 on 2020-09-05 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
        ('pwn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('total', models.FloatField()),
                ('status', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('address', models.TextField()),
                ('items', models.ManyToManyField(to='vendor.FoodItemsModel')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRegistrationModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField(unique=True)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=20)),
                ('OTP', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pwn.CityModel')),
            ],
        ),
    ]
