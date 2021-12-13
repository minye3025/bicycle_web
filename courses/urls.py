from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:courseinfo_id>/', views.detail, name='detail'),
    # path('<int:boardID>/', views.detail),
]