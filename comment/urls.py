from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comment.views import *

urlpatterns = [
    path('post/<int:pk>/comment', CommentListView.as_view()),
    path('comment/<int:pk>', CommentDetailView.as_view())
]