from django.db import models
from django import forms

class Сhairman(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phones_num = models.CharField(max_length=200)
    e_mail = models.EmailField()
    chairman_photo = models.ImageField(default=1)
    slug = models.SlugField(max_length=100)


    def __str__(self):
        return self.name

class Appeal(models.Model):
    name = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=30)
    filial = models.CharField(max_length=20)
    message = models.TextField()
    appeal = models.Manager()


class Document(models.Model):
    date_append = models.DateTimeField('date published')
    document = models.FileField()
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.slug


class Employee(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phones_num = models.CharField(max_length=200)
    e_mail = models.EmailField()
    employee_photo = models.ImageField(default=1)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    news_date = models.DateTimeField('date published')
    news_text = models.TextField()
    news_photo = models.ImageField()
    slug = models.SlugField(max_length=100)


    def __str__(self):
        return self.news_text


class ShortNewsOnMainPage(models.Model):
    short_news_text = models.TextField()
    short_news_photo = models.ImageField(upload_to='images/news/')
    short_news_header = models.CharField(max_length=30, default="Заголовок")
    sh_news = models.Manager()

    @property
    def photo_url(self):
        if self.short_news_photo and hasattr(self.short_news_photo, 'url'):
            return self.short_news_photo.url

    def __str__(self):
        return self.short_news_header