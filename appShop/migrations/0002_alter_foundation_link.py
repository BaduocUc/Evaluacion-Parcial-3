# Generated by Django 4.1.2 on 2024-07-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appShop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foundation',
            name='link',
            field=models.URLField(),
        ),
    ]