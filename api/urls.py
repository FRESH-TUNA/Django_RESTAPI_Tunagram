from django.urls import path, include, re_path

urlpatterns = [
    path('tunagramAuth/', include('tunagramAuth.urls')),
    path('', include('post.urls')),
    path('', include('comment.urls')),
]