# Generated by Django 4.1.4 on 2022-12-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.FileField(null=True, upload_to='profile'),
        ),
    ]