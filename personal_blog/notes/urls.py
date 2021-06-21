from django.urls import path
from .views import FileCleanFunction, NoteDeleteFunction, NoteUpdateFunction, NoteCreateFunction, TopicUpdateView, TopicDeleteFunction, TopicDetailView, TopicCreateView , TopicListView, NoteDetailFunction
urlpatterns = [
    path('', TopicListView.as_view(), name='topic_list'),
    path('create_topic/', TopicCreateView.as_view(), name="create_topic"),
    path('<uuid:pk>/delete_topic', TopicDeleteFunction, name="delete_topic"),
    path('<uuid:pk>/update_topic', TopicUpdateView.as_view(), name="update_topic"),
    path('<uuid:pk>', TopicDetailView.as_view(), name="topic_detail"),

    path('<uuid:pk>/create_note', NoteCreateFunction, name="create_note"),
    path('<uuid:topic_pk>/<uuid:note_pk>', NoteDetailFunction, name="note_detail"),
    path('<uuid:topic_pk>/<uuid:note_pk>/update_note', NoteUpdateFunction, name="update_note"),
    path('<uuid:topic_pk>/<uuid:note_pk>/delete_note', NoteDeleteFunction, name="delete_note"),
    path('clean_file/', FileCleanFunction, name='clean_file'),
]