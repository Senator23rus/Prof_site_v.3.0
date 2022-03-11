# Generated by Django 4.0.2 on 2022-03-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_append', models.DateTimeField(verbose_name='date published')),
                ('document', models.FileField(upload_to='')),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phones_num', models.CharField(max_length=200)),
                ('e_mail', models.EmailField(max_length=254)),
                ('employee_photo', models.ImageField(default=1, upload_to='')),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_date', models.DateTimeField(verbose_name='date published')),
                ('news_text', models.TextField()),
                ('news_photo', models.ImageField(upload_to='')),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShortNewsOnMainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_news_text', models.TextField()),
                ('short_news_photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Сhairman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phones_num', models.CharField(max_length=200)),
                ('e_mail', models.EmailField(max_length=254)),
                ('chairman_photo', models.ImageField(default=1, upload_to='')),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
    ]