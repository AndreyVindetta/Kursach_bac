# здесь хранятся различные таблицы, которые мы будем добавлять в базу данных
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Client(models.Model):
    FIO = models.CharField('ФИО', max_length=250)
    address = models.CharField('Адрес', max_length=250)
    number_phone = models.CharField('Номер телефона', max_length=250)
    email = models.CharField('email', max_length=250)
    gender = models.CharField('Пол', max_length=250)
    policyStatus = models.CharField('Статус полиса', max_length=250)
    insuranceType = models.CharField('Тип страхования', max_length=250)
    insuranceAmount = models.CharField('Сумма страхования', max_length=250)
    startDate = models.CharField('Начало страхования', max_length=250)
    endDate = models.CharField('Конец страхования', max_length=250)
    premium = models.CharField('Сумма, которую выплачивает клиент', max_length=250)


def __str__(self):
    return self.FIO


class Meta:
    verbose_name = 'Клиента'
    verbose_name_plural = 'Клиенты'
