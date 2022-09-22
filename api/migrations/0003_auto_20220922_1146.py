# Generated by Django 3.2.15 on 2022-09-22 08:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220921_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterField(
            model_name='car',
            name='end_year',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator(message='Значение не является годом от 1900 до 2099!', regex='^(19|20)\\d{2}$')], verbose_name='Год окончания выпуска'),
        ),
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='car',
            name='start_year',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator(message='Значение не является годом от 1900 до 2099!', regex='^(19|20)\\d{2}$')], verbose_name='Год начала выпуска'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Название'),
        ),
    ]