from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('calendar', views.calendar, name='calendar'),
    path('entry/add', views.add, name='add'),
    path('entry/<int:pk>/', include([
        path('', views.details, name='details'),
        path('delete/', views.delete, name='delete'),
    ]))

]