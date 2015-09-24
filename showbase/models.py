# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vedomost(models.Model):
	name_v = models.CharField(max_length = 50,verbose_name='Тип ведомости')
	class Meta:
		verbose_name = 'Ведомости'
		verbose_name_plural = 'Ведомости'

	def __unicode__(self):
		return self.name_v

class Check(models.Model):
	name_c = models.CharField(max_length = 50,verbose_name='Отметки')
	date_inv =  models.DateField(auto_now=False,blank=True,null=True,verbose_name='Дата')
	class Meta:
		verbose_name = 'Отметки'
		verbose_name_plural = 'Отметки'

	def __unicode__(self):
		return self.name_c

class Place(models.Model):
	name_c = models.CharField(max_length = 50,verbose_name='Аудитория')
	class Meta:
		verbose_name = 'Место установки'
		verbose_name_plural = 'Место установки'

	def __unicode__(self):
		return self.name_c

class Persons(models.Model):
	name_c = models.CharField(max_length = 50,verbose_name='Подотчетное лицо')
	class Meta:
		verbose_name = 'Подотчетное лицо'
		verbose_name_plural = 'Подотчетные лица'

	def __unicode__(self):
		return self.name_c

class Otmetka(models.Model):
    otmetka = models.SlugField(verbose_name='Изменения',blank=True,null=True)
    date_inv =  models.DateField(auto_now=False,blank=True,null=True,verbose_name='Дата события')
    class Meta:
        verbose_name = 'Отметка'
        verbose_name_plural = 'Отметки'

	def __unicode__(self):
		return self.name_c

class Podotchet(models.Model):
	list_t = models.ForeignKey(Vedomost,verbose_name='Ведомость',blank=True,null=True)
	name_el = models.CharField(max_length = 50,verbose_name='Наименование')
	date_now =  models.DateField(auto_now=True,blank=True,null=True,verbose_name='Дата изменения')
	date_inv =  models.DateField(auto_now=False,blank=True,null=True,verbose_name='Дата инвентаризации')
	date_spis =  models.DateField(auto_now=False,blank=True,null=True,verbose_name='Дата списания')
	inv_number = models.CharField(max_length = 15,verbose_name='Инвентарный номер',blank=True)
	price=models.DecimalField(max_digits = 7, decimal_places=2,verbose_name='Цена',blank=True,null=True)
	person = models.ForeignKey(Persons, null=True, blank=True, verbose_name=u'Подотчетное лицо')
	place = models.ForeignKey(Place, verbose_name='Место установки',blank=True,null=True)
	comment = models.TextField(verbose_name='Дополнительная информация',blank=True,null=True)
	inv = models.BooleanField(verbose_name='Инвентаризировано',default=False)	
	otmetka = models.ForeignKey(Otmetka, verbose_name='Изменения, перемещения',blank=True,null=True)
	spisano = models.BooleanField(verbose_name='Списано',default=False)
	author = models.ForeignKey(User, null = True, blank = True ,editable=False, verbose_name=u'Автор')
	class Meta:
		verbose_name = 'Объект подотчета'
		verbose_name_plural = 'Подотчетная ведомость'



