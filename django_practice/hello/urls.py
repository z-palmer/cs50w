from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zach', views.zach, name='zach'),
    path('<str:name>', views.greet, name='greet')
]
