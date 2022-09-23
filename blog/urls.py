from django.urls import path
from blog import views as user_views
from .views import PostDetailView,PostListView,PostCreateView,PostUpdateView,PostDeleteView,about, filterListView,filterListView

urlpatterns = [
    path("", PostListView.as_view(), name='blog-home'),
    path("post/<int:pk>/",PostDetailView.as_view(), name='post-detail'),
    path("post/new/",PostCreateView.as_view(), name='post-create'),
    path("post/<int:pk>/update/",PostUpdateView.as_view(), name='post-update'),
    path("post/<int:pk>/delete/",PostDeleteView.as_view(), name='post-delete'),
    path("about/",user_views.about, name="blog-about"),
    path("/<str:name>", filterListView.as_view(), name='filter'),

]