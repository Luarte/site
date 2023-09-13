# Generated by Django 4.2 on 2023-04-21 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_remove_product_modl_modl_model_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modl",
            name="company_name",
            field=models.CharField(
                choices=[("ht", "Hypertherm"), ("ct", "Centricut")],
                max_length=200,
                verbose_name="Имя компании",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="Модель оборудования",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="models",
                to="products.modl",
            ),
        ),
    ]
