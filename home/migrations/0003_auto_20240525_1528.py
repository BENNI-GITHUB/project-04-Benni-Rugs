# Generated by Django 3.2.25 on 2024-05-25 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20240525_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribers',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
