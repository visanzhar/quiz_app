# Generated by Django 4.1.6 on 2023-05-25 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choices',
        ),
    ]
