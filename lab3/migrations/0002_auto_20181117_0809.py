# Generated by Django 2.1.2 on 2018-11-17 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Latitude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Longitude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MeasureDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.MeasureDate')),
                ('lat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.Latitude')),
                ('lon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.Longitude')),
            ],
        ),
        migrations.DeleteModel(
            name='GeoTemperature',
        ),
    ]