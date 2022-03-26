# Generated by Django 4.0.2 on 2022-03-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_alter_document_date_append_alter_news_news_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='date_append',
        ),
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default='Название', max_length=50),
        ),
        migrations.AddField(
            model_name='document',
            name='text_name',
            field=models.CharField(default='Введение дата', max_length=200),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/'),
        ),
    ]