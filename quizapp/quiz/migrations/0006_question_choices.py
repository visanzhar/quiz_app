# Generated by Django 4.1.6 on 2023-05-25 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_remove_question_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(related_name='questions', to='quiz.quizchoice'),
        ),
    ]