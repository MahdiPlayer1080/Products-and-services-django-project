# Generated by Django 4.2.2 on 2023-06-16 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to='user'),
        ),
    ]
