from django.urls import path
from .views import quiz_list, quiz_detail

app_name = 'quiz'

urlpatterns = [
    path('', quiz_list, name='quiz_list'),
    path('<int:quiz_id>/', quiz_detail, name='quiz_detail'),
]