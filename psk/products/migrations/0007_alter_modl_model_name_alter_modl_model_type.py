# Generated by Django 4.2 on 2023-04-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_alter_modl_company_name_alter_modl_model_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modl",
            name="model_name",
            field=models.SlugField(max_length=500, verbose_name="Имя модели"),
        ),
        migrations.AlterField(
            model_name="modl",
            name="model_type",
            field=models.CharField(
                choices=[("ls", "Лазер"), ("pl", "Плазма"), ("wd", "Сварка")],
                default="ls",
                max_length=10,
                verbose_name="Тип",
            ),
        ),
    ]