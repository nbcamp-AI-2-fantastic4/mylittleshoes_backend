from django.urls import path
from upload import views

urlpatterns = [
    # upload/
    path('', views.ImageUploadView.as_view()),
    path('result/', views.ImageResultView.as_view()),
]
