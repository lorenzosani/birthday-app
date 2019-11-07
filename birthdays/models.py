from django.db import models
from datetime import date

class Person(models.Model):
    name = models.CharField(max_length=200)
    picture = models.URLField(max_length=400)
    fun_fact = models.CharField(max_length=300)
    birth_date = models.DateField()

    def isBirthdayToday(self):
	    return date.today().month==self.birth_date.month and date.today().day==self.birth_date.day


class Present(models.Model):
    recipient = models.ForeignKey(Person, on_delete=models.CASCADE)
    what = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
