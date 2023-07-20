# Generated by Django 4.2 on 2023-04-24 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gols',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(default='Serie A', max_length=5000)),
                ('nomeGiocatore', models.CharField(default='Serie A', max_length=100)),
                ('squadra', models.CharField(default='Serie A', max_length=100)),
                ('partita', models.CharField(default='Serie A', max_length=100)),
                ('giornata', models.CharField(default='Serie A', max_length=100)),
                ('ora', models.TimeField(choices=[(datetime.time(10, 0), '10:00'), (datetime.time(11, 0), '11:00'), (datetime.time(12, 0), '12:00'), (datetime.time(13, 0), '13:00'), (datetime.time(14, 0), '14:00'), (datetime.time(15, 0), '15:00'), (datetime.time(16, 0), '16:00'), (datetime.time(17, 0), '17:00'), (datetime.time(18, 0), '18:00'), (datetime.time(18, 30), '18:30'), (datetime.time(19, 0), '19:00'), (datetime.time(20, 0), '20:00'), (datetime.time(21, 0), '21:00')], default=datetime.time(12, 0))),
                ('competizione', models.CharField(choices=[('Serie A', 'Serie A'), ('Serie B', 'Serie B'), ('Mondiali 2006', 'Mondiali 2006')], default='Serie A', max_length=100)),
                ('descrizioneGoal', models.CharField(choices=[('Testa', 'Testa'), ('Rigore', 'Rigore'), ('Al volo', 'Al volo'), ('GDM', 'GDM'), ('Tiro da fuori', 'Tiro da fuori'), ('Tiro in area', 'Tiro in area'), ('Punizione', 'Punizione'), ('Dribling sul portiere', 'Dribling sul portiere')], default='Serie A', max_length=500)),
                ('minutoGoal', models.IntegerField(default=1)),
                ('stagione', models.CharField(choices=[('2022/2023', '2022/2023'), ('2021/2022', '2021/2022'), ('2006/2007', '2006/2007')], default='Serie A', max_length=100)),
                ('valutazione', models.CharField(choices=[('1 stella', '1 stella'), ('2 stelle', '2 stelle'), ('3 stelle', '3 stelle'), ('4 stelle', '4 stelle'), ('5 stelle', '5 stelle')], default='Serie A', max_length=100)),
                ('data', models.CharField(default='0000-00-00', max_length=100)),
            ],
            options={
                'unique_together': {('partita', 'data')},
            },
        ),
    ]
