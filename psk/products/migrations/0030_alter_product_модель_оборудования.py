# Generated by Django 4.2 on 2023-08-20 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0029_alter_product_модель_оборудования'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Модель оборудования',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='products',
                to='products.modl',
            ),
        ),
    ]
