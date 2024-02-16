from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (PostListView, PostDetailView, PostCreateView, PostDeleteView,
                    PostUpdateView, MessageListView, MessageCreateView, MessageDeleteView, CategoryView,
                    ProfileView, MessageDetailView)


urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_one'),
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update_post'),
    path('message/', MessageListView.as_view(), name='messages'),
    path('message_one/<int:pk>/', MessageDetailView.as_view(), name='one_message'),
    path('<int:pk>/message/create/', MessageCreateView.as_view(), name='create_message'),
    path('message/delete/', MessageDeleteView.as_view(), name='delete_message'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category_list'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='name_profile'),
]
