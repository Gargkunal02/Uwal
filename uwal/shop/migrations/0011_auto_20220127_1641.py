# Generated by Django 3.0.7 on 2022-01-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_image3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
