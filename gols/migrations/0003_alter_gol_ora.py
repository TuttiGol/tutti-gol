# Generated by Django 4.2 on 2023-04-25 22:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gols', '0002_gol_delete_gols'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gol',
            name='ora',
            field=models.TimeField(choices=[(datetime.time(10, 0), '10:00'), (datetime.time(11, 0), '11:00'), (datetime.time(12, 0), '12:00'), (datetime.time(12, 30), '12:30'), (datetime.time(13, 0), '13:00'), (datetime.time(14, 0), '14:00'), (datetime.time(15, 0), '15:00'), (datetime.time(16, 0), '16:00'), (datetime.time(17, 0), '17:00'), (datetime.time(18, 0), '18:00'), (datetime.time(18, 30), '18:30'), (datetime.time(19, 0), '19:00'), (datetime.time(20, 0), '20:00'), (datetime.time(21, 0), '21:00')], default=datetime.time(12, 0)),
        ),
    ]
