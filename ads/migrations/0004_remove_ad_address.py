# Generated by Django 4.0.4 on 2022-05-12 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_ad_category_ad_image_alter_ad_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='address',
        ),
    ]