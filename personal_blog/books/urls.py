from django.urls import path
from .views import ChapterDeleteFunction, ChapterUpdateFunction, ChapterCreateFunction, BookUpdateView, BookDeleteFunction, BookDetailView, BookCreateView , BookListView, ChapterDetailFunction
urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('create_book/', BookCreateView.as_view(), name="create_book"),
    path('<uuid:pk>/delete_book', BookDeleteFunction, name="delete_book"),
    path('<uuid:pk>/update_book', BookUpdateView.as_view(), name="update_book"),
    path('<uuid:pk>', BookDetailView.as_view(), name="book_detail"),

    path('<uuid:pk>/create_chapter', ChapterCreateFunction, name="create_chapter"),
    path('<uuid:book_pk>/<uuid:chapter_pk>', ChapterDetailFunction, name="chapter_detail"),
    path('<uuid:book_pk>/<uuid:chapter_pk>/update_chapter', ChapterUpdateFunction, name="update_chapter"),
    path('<uuid:book_pk>/<uuid:chapter_pk>/delete_chapter', ChapterDeleteFunction, name="delete_chapter"),
]