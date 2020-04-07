from django.urls import path, reverse_lazy

#from .views import message_to_user, message_sent

from .views import (
    BlogListView,
    BlogUpdateView,
    BlogDetailView,
    BlogCreateView,
    BlogDeleteView,
    ProjectListView,
    ProjectDetailView,
    reviews,
    aboutView
    
    
)
urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('review', reviews, name='review'),
    path('', BlogListView.as_view(), name='home'),
    path('project', ProjectListView.as_view(), name='project'),
    path('about/', aboutView, name='about'),

    
]
