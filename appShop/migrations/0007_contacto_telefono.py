# Generated by Django 4.1.2 on 2024-07-11 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appShop', '0006_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
    ]