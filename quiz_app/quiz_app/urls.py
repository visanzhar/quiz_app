# # from django.urls import path, include
# # # from quiz.views import quiz
# # from quiz.views import QuizView, ResultView

# # from django.contrib import admin

# # urlpatterns = [
# #     # path('', quiz, name='quiz'),
# #     path('', QuizView.as_view(), name='quiz'),
# #     path('result/', ResultView.as_view(), name='result'),
# #     path('admin/', admin.site.urls),
# #     path('quiz/', include('quiz.urls')),
    
# # ]


# from django.urls import path
# from quiz.views import question_list, result, QuizView, ResultView


# urlpatterns = [
#     path('', question_list, name='question_list'),
#     path('result/', result, name='result'),
#     path('quiz/', QuizView.as_view(), name='quiz'),
#     path('result/details/', ResultView.as_view(), name='result_details'),
# ]


from django.contrib import admin
from django.urls import include, path

from quiz.views import question_list, quiz_result, QuizView, ResultView, quiz
# from ./quiz import views

urlpatterns = [
    path('', question_list, name='question_list'),
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),
    path('quiz/', quiz, name='quiz'),
    path('result/', quiz_result, name='result'),
    
]
