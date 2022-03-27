from django.db import models
from django import forms


class Сhairman(models.Model):
    name = models.CharField(max_length=200)
    name_organisation = models.CharField(max_length=200,default="Название" )
    position = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phones_num = models.CharField(max_length=200)
    e_mail = models.EmailField()
    chairman_photo = models.ImageField(default=1, upload_to='images/Chairmans/')
    slug = models.SlugField(max_length=100)
    chairman_object = models.Manager()

    def __str__(self):
        return self.name


class Appeal(models.Model):
    name = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=30)
    filial = models.CharField(max_length=20)
    message = models.TextField()
    appeal = models.Manager()


class Document(models.Model):
    name = models.CharField(max_length=50, default="Название")
    text_name = models.CharField(max_length=200, default="Введение дата")
    document = models.FileField(upload_to='documents')
    slug = models.SlugField(max_length=100)
    doc_object = models.Manager()

    @property
    def photo_url(self):
        if self.document and hasattr(self.document, 'url'):
            return self.document.url

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
    news_title = models.CharField(max_length=255, default='название новости')
    news_date = models.DateField('date published')
    news_text = models.TextField()
    news_photo = models.ImageField(upload_to='images/page_news/')
    slug = models.SlugField(max_length=100)
    news_object = models.Manager()

    def __str__(self):
        return self.news_title


class ShortNewsOnMainPage(models.Model):
    short_news_text = models.TextField()
    short_news_photo = models.ImageField(upload_to='images/main_news/')
    short_news_header = models.CharField(max_length=30, default="Заголовок")
    sh_news = models.Manager()

    @property
    def photo_url(self):
        if self.short_news_photo and hasattr(self.short_news_photo, 'url'):
            return self.short_news_photo.url

    def __str__(self):
        return self.short_news_header
