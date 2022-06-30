# from django.contrib import admin
from django.urls import path, include
from recommend import views

urlpatterns = [
    # recommend/
    path('', views.RecommendViewAll.as_view()),
    path('brand/', views.RecommendViewBrand.as_view()),
    path('color/', views.RecommendViewColor.as_view()),
    path('height/', views.RecommendViewHeight.as_view()),
]
