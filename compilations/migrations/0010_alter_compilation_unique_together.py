# Generated by Django 4.2 on 2023-05-08 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compilations', '0009_alter_compilation_descrizionegoal'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='compilation',
            unique_together=set(),
        ),
    ]
