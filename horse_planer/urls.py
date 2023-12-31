from . import views
from django.urls import path
from .views import filter_posts


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('post-detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('horses/', views.HorsesView.as_view(), name='horses'),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('filter/', filter_posts, name='filter_posts'),
]
