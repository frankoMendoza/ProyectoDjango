# Generated by Django 2.1.2 on 2019-01-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0004_auto_20190114_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estadoCivil',
            field=models.CharField(choices=[('c', 'Casado'), ('s', 'Soltero'), ('d', 'Divorciado'), ('e', 'Sin especificar')], max_length=15),
        ),
    ]
