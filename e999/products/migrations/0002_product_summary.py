# Generated by Django 3.1.3 on 2021-07-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='this is coool'),
        ),
    ]
