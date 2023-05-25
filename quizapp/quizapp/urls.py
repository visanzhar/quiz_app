from django.urls import path, include
from quiz.views import quiz_list, quiz_detail
from django.contrib import admin

urlpatterns = [
    path('quiz/', quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', quiz_detail, name='quiz_detail'),
    path('admin/', admin.site.urls),
]