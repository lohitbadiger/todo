
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deleteComplete', views.deleteCompleted, name='delete'),
    path('deleteAdd', views.deleteAdd, name='deleteAdd'),

    



]
