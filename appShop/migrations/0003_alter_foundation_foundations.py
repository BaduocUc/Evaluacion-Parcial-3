# Generated by Django 4.1.2 on 2024-07-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appShop', '0002_alter_foundation_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foundation',
            name='foundations',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]