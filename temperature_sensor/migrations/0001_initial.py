# Generated by Django 3.1.7 on 2021-03-01 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sensor_unit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemperatureSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('temperature', models.DecimalField(decimal_places=1, default=20, max_digits=4)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor_unit.sensorunit')),
            ],
        ),
    ]
