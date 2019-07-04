from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views import PostViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'post', PostViewSet, basename='post')

urlpatterns = router.urls