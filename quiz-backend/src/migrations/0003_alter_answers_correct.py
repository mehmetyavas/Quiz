# Generated by Django 4.1 on 2022-08-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='correct',
            field=models.BooleanField(default=False),
        ),
    ]
