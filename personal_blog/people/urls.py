from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create_post', PostCreateView.as_view(), name='create_post'),
    path('<uuid:pk>/update_post', PostUpdateView.as_view(), name='update_post'),
    path('<uuid:pk>/delete_post', PostDeleteView.as_view(), name='delete_post'),
]