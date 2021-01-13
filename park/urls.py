from django.urls import path

from park import views
from main_app.services import Services

app_name = 'park'

urlpatterns = [
    path('create/', views.CreateParkView.as_view(), name='create'),
    path('all/', Services.get_all_parks)
]
