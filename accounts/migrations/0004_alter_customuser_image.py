# Generated by Django 4.2.2 on 2023-06-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='Default.jpg', upload_to='user'),
        ),
    ]
