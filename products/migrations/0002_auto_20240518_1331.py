# Generated by Django 3.2.25 on 2024-05-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]