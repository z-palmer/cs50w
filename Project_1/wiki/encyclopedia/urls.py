from django.urls import path

from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name='index'),
    path('new/', views.new_entry, name='new'),
    path('wiki/<str:name>/', views.entry, name='entry'),
    path('edit/<str:name>/', views.edit, name='edit'),
    path('random/', views.random_entry, name='random'),
    path('search/', views.search, name='search'),
]
