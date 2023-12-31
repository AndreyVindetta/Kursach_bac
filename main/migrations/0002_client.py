# Generated by Django 5.0 on 2023-12-18 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=250, verbose_name='ФИО')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('number_phone', models.CharField(max_length=250, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=250, verbose_name='email')),
                ('gender', models.CharField(max_length=250, verbose_name='Пол')),
                ('policyStatus', models.CharField(max_length=250, verbose_name='Статус полиса')),
                ('insuranceType', models.CharField(max_length=250, verbose_name='Тип страхования')),
                ('insuranceAmount', models.CharField(max_length=250, verbose_name='Сумма страхования')),
                ('startDate', models.CharField(max_length=250, verbose_name='Начало страхования')),
                ('endDate', models.CharField(max_length=250, verbose_name='Конец страхования')),
                ('premium', models.CharField(max_length=250, verbose_name='Сумма, которую выплачивает клиент')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
