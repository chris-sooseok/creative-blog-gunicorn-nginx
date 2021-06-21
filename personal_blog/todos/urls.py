from django.urls import path
from .views import TodoUpdateFunction, DateListView, DateDetailView, DateCreateView, DateDeleteView, TodoCreateFunction, TodoDeleteFunction

urlpatterns = [
    path('', DateListView.as_view(), name='date_list'),
    path('<uuid:pk>', DateDetailView.as_view(), name='date_detail'),
    path('create_date', DateCreateView.as_view(), name='create_date'),
    path('delete_date/<uuid:pk>', DateDeleteView.as_view(), name='delete_date'),
    path('create_todo/<uuid:pk>', TodoCreateFunction, name='create_todo'),
    path('delete_todo/<uuid:date_pk>/<int:todo_pk>', TodoDeleteFunction, name='delete_todo'),
    path('update_todo/<uuid:date_pk>/<int:todo_pk>', TodoUpdateFunction, name='update_todo'),
]