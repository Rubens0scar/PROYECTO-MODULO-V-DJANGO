# Generated by Django 4.1.2 on 2022-10-05 16:48

import appmed.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmed', '0004_alter_paciente_estado_civil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='codigo',
            field=models.CharField(max_length=35, validators=[appmed.validators.validar_codigo_paciente, appmed.validators.validar_codigo]),
        ),
    ]
