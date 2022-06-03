# Generated by Django 4.0.4 on 2022-06-03 13:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_alter_selection_options_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=10, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]