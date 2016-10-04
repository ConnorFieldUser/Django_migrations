from django.db import models

# Create your models here.


class Fighter(models.Model):

    rank = models.IntegerField()
    last_name = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    fights = models.IntegerField()
    strikes = models.IntegerField()
    str_accuracy = models.CharField(max_length=15)
    takedowns = models.IntegerField()
    td_accuracy = models.CharField(max_length=15)
    knockdowns = models.IntegerField()
    reversals = models.IntegerField()
    passes = models.IntegerField()
    submissions = models.IntegerField()

# class Team(models.Model):
#     name = models.CharField(max_length=100)
#     year = models.IntegerField()
#     captain = models.ForeignKey(Person)
