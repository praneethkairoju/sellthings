# Generated by Django 3.1.2 on 2021-10-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
    ]
