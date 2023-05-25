from django.shortcuts import render, redirect
from .models import Question, Answer


def question_list(request):
    questions = Question.objects.all()

    if request.method == 'POST':
        selected_answers = request.POST.getlist('answer')
        # Further processing of selected answers...

        # Redirect to the results view
        return redirect('result')

    context = {'questions': questions}
    return render(request, 'quiz.html', context)


from django.shortcuts import render

def quiz(request):
    # Add your logic here
    return render(request, 'quiz.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.sessions.models import Session

def quiz_result(request):
    if request.method == 'POST':
        choices = request.POST.getlist('choice')
        correct_answers = Answer.objects.filter(is_correct=True).values_list('id', flat=True)
        user_score = sum(int(choice) in correct_answers for choice in choices)
        request.session['score'] = user_score
        return redirect('result')


def result(request):
    if request.method == 'POST':
        selected_choices = request.POST.getlist('choice')
        correct_answers = Answer.objects.filter(is_correct=True).values_list('id', flat=True)
        score = sum(1 for choice in selected_choices if int(choice) in correct_answers)
        return render(request, 'result.html', {'score': score})
    else:
        score = request.session.get('score', 0)
        del request.session['score']  # Remove the score from the session
        return render(request, 'result.html', {'score': score})




def calculate_score(selected_answers):
    # Implement your logic to calculate the quiz score based on the selected choices
    # Return the calculated score
    pass

def save_quiz_results(user, score):
    # Implement your logic to save the quiz results for the user
    pass

def get_quiz_results(user):
    # Implement your logic to retrieve the quiz results for the user
    # Return the quiz results
    pass

from django.shortcuts import render
from django.views import View

class QuizView(View):
    def get(self, request):
        # Logic for displaying the quiz
        return render(request, 'quiz.html')

class ResultView(View):
    def get(self, request):
        # Logic for displaying the quiz results
        return render(request, 'result.html')
