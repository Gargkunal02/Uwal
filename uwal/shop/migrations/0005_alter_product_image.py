# Generated by Django 4.0 on 2022-01-03 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/static/Base/img/bg-img/bg-1.jpg', upload_to='upload/products/'),
        ),
    ]