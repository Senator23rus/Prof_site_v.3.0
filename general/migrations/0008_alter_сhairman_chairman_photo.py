# Generated by Django 4.0.2 on 2022-03-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_alter_сhairman_managers_сhairman_name_organisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сhairman',
            name='chairman_photo',
            field=models.ImageField(default=1, upload_to='images/Chairmans/'),
        ),
    ]
