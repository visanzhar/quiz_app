# Generated by Django 4.1.6 on 2023-05-25 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quizquestion_quizchoice'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
