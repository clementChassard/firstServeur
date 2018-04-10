from django.urls import path

from . import views


app_name = 'monApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('brokenpage', views.brokenpage, name='brokenpage'),
    path('nothing', views.nothing, name='nothing'),
]


