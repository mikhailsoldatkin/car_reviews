# Generated by Django 3.2.15 on 2022-09-21 10:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='end_year',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator(message='Значение не является годом в формате четырёх цифр!', regex='^(19|20)\\d{2}$')], verbose_name='Год окончания выпуска'),
        ),
        migrations.AlterField(
            model_name='car',
            name='start_year',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator(message='Значение не является годом в формате четырёх цифр!', regex='^(19|20)\\d{2}$')], verbose_name='Год начала выпуска'),
        ),
    ]
