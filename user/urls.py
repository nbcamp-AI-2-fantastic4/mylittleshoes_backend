from django.urls import path, include
from . import views

# user/
urlpatterns = [
    path('login/', views.UserView.as_view()),
    path('logout/', views.UserView.as_view()),
    path('info/', views.UserInfoView.as_view()),
]
