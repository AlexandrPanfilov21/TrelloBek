from django.urls import path

from user.views import UserByToken

urlpatterns = [
    path('user/token/', UserByToken.as_view()),
]