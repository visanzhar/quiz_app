from django.shortcuts import render
from .models import Quiz


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})


def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = quiz.questions.all()

    context = {
        'quiz': quiz,
        'questions': questions,
    }

    return render(request, 'quiz/quiz_detail.html', context)