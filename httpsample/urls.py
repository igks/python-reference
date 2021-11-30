from django.urls import path
from . import views

app_name = 'httpsample'
urlpatterns = [
    path('', views.get, name='get'),
    path('/add', views.add, name='add'),
    path('/edit', views.edit, name='edit'),
    path('/delete', views.delete, name='delete')
]