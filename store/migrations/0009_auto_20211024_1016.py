# Generated by Django 3.1.2 on 2021-10-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20211024_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='id',
        ),
        migrations.AddField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default=1, max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
