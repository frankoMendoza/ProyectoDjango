# Generated by Django 2.1.2 on 2019-01-17 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0007_auto_20190117_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaccion',
            name='cuenta_destino',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estadoCivil',
            field=models.CharField(choices=[('d', 'Divorciado'), ('c', 'Casado'), ('s', 'Soltero'), ('e', 'Sin especificar')], max_length=15),
        ),
    ]
