# Generated by Django 4.2 on 2023-08-19 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0020_alter_company_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'type_name',
                    models.CharField(
                        max_length=50, verbose_name='Название типа'
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name='modl',
            name='model_type',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='models',
                to='products.type',
            ),
        ),
    ]
