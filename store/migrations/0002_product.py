# Generated by Django 3.1.2 on 2021-10-23 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('Descreption', models.TextField(max_length=400)),
                ('price', models.IntegerField(default=199)),
                ('category_id', models.ForeignKey(default='doors', on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]
