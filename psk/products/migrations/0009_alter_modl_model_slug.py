# Generated by Django 4.2 on 2023-04-21 16:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0008_modl_model_slug_alter_modl_model_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modl",
            name="model_slug",
            field=models.SlugField(null=True, verbose_name="Ссылка на модель"),
        ),
    ]
