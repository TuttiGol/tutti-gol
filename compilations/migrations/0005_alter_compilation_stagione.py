# Generated by Django 4.2 on 2023-05-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compilations', '0004_alter_compilation_competizione_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compilation',
            name='stagione',
            field=models.CharField(blank=True, choices=[('2022/2023', '2022/2023'), ('2021/2022', '2021/2022'), ('2009/2010', '2009/2010'), ('2006/2007', '2006/2007'), ('2001/2002', '2001/2002')], max_length=100),
        ),
    ]