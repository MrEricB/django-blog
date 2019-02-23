from django.contrib import admin
from django.urls import path, include
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('<int:user_id>', views.dashboard_home, name='dashboard_home'),
    path('charts/<int:user_id>', views.dashboard_charts, name='charts')
]