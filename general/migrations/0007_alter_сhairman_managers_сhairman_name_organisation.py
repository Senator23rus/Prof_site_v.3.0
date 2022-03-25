# Generated by Django 4.0.2 on 2022-03-25 16:13

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_alter_document_managers_alter_news_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='сhairman',
            managers=[
                ('chairman_object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='сhairman',
            name='name_organisation',
            field=models.CharField(default='Название', max_length=200),
        ),
    ]
