# Generated by Django 3.2.25 on 2024-04-14 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
