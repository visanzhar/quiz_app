# from django.urls import path
# from .views import question_list, result

# app_name = 'quiz'

# urlpatterns = [
#     path('', question_list, name='quiz'),
#     path('result/', result, name='result'),
# ]

from django.urls import path
from .views import question_list, result

app_name = 'quiz'

urlpatterns = [
    path('', question_list, name='quiz'),
    path('result/', result, name='result'),
    
]
