# Generated by Django 3.1.7 on 2021-03-03 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='activity date')),
                ('activity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('depart', models.DateField(verbose_name='departure date')),
                ('arrive', models.DateField(verbose_name='arrival date')),
                ('hotel', models.CharField(max_length=100)),
                ('budget', models.IntegerField()),
                ('description', models.TextField(max_length=250)),
                ('friends', models.ManyToManyField(to='main_app.Friend')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.trip')),
            ],
        ),
    ]