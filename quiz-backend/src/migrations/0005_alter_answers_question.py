# Generated by Django 4.1 on 2022-08-15 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_alter_answers_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='src.questions'),
        ),
    ]
