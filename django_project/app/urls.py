from django.urls import path
from . import views

# 여기서 name은 url의 닉네임 같은 개념
# 예를 들어 baseUrl = "www.example.com이라면"
# 아래 urlpatterns 배열에 존재하는 path의 경우 "www.example.com/home" == "www.example.com"과 같은 개념이다.
urlpatterns = [
    path('', views.index, name="index")
]