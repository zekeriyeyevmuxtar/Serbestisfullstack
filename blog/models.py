from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Mehsul kataqorisi')

class Mehsullar(models.Model):
    name = models.CharField(max_length=100, verbose_name='Mehsul adi')
    cost = models.IntegerField(verbose_name='Qiymet')
    desc = models.CharField(max_length=100, verbose_name='Mehsul haqqinda')
    date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(verbose_name="Sekil")
    catagories= models.ForeignKey()


class Home(models.Model):
    title = models.CharField(max_length=100, verbose_name='Basliq')
    text = models.TextField(verbose_name='Text')


class Haqqimizda(models.Model):
    about = models.TextField(verbose_name='Haqqimizda texti')
    mission = models.TextField(verbose_name='Missiyamız və Vizyonumuz texti')

class Team(models.Model):
    name = models.CharField(verbose_name="Adi ve soyadi", max_length=100)
    image = models.FileField(verbose_name="sekil")
    position = models.CharField(verbose_name="Vezife", max_length=100)
    detail = models.TextField(verbose_name="Haqqinizda")
    email = models.CharField(max_length=100, verbose_name='mail address')

# Create your models here.
