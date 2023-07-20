# Generated by Django 4.2 on 2023-05-08 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compilations', '0008_remove_compilation_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compilation',
            name='descrizioneGoal',
            field=models.CharField(blank=True, choices=[('Testa', 'Testa'), ('Rigore', 'Rigore'), ('Al volo', 'Al volo'), ('GDM', 'GDM'), ('Tiro da fuori', 'Tiro da fuori'), ('Tiro in area', 'Tiro in area'), ('Punizione', 'Punizione'), ('Dribling sul portiere', 'Dribling sul portiere'), ('Pallonetto', 'Pallonetto'), ('Autogol', 'Autogol'), ('Coast to coast', 'Coast to coast')], max_length=500),
        ),
    ]
