# Generated by Django 4.0.1 on 2022-01-27 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_category_id_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='upload/products/no-preview.png', upload_to='upload/products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='upload/products/no-preview.png', upload_to='upload/products2/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(default='upload/products/no-preview.png', upload_to='upload/products3/'),
        ),
    ]
