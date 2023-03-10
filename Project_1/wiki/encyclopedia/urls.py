from django.urls import path, include

from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name='index'),
    path('new/', views.new_entry, name='new'),
    path('wiki/<str:name>/', views.entry, name='entry'),
]
