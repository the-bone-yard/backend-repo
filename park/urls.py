from django.urls import path

from park import views

app_name = 'park'

urlpatterns = [
    path('create/', views.CreateParkView.as_view(), name='create'),
]