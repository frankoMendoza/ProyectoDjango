# Generated by Django 2.1.2 on 2019-01-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0005_auto_20190114_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estadoCivil',
            field=models.CharField(choices=[('e', 'Sin especificar'), ('s', 'Soltero'), ('d', 'Divorciado'), ('c', 'Casado')], max_length=15),
        ),
    ]
