# Generated by Django 4.0.2 on 2022-03-01 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='full_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='сhairman',
            old_name='full_name',
            new_name='name',
        ),
    ]