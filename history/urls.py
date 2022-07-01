
from django.contrib import admin
from django.urls import path, include
from . import views

# history/
urlpatterns = [
    path('', views.HistoryView.as_view()),
    path('comment/', views.CommentView.as_view()),
    path('comment/<comment_id>/', views.CommentView.as_view()),
    path('like/<history_id>', views.LikeView.as_view()),
]
