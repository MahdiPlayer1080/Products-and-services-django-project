# Generated by Django 4.2.2 on 2023-06-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='user'),
        ),
    ]
