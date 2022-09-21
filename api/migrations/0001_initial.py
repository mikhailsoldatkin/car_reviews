# Generated by Django 3.2.15 on 2022-09-21 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('start_year', models.PositiveIntegerField(verbose_name='Год начала выпуска')),
                ('end_year', models.PositiveIntegerField(verbose_name='Год окончания выпуска')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manufacturers', to='api.country', verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_email', models.EmailField(max_length=254, verbose_name='Email Автора')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.car', verbose_name='Автомобиль')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='api.manufacturer', verbose_name='Производитель'),
        ),
    ]
