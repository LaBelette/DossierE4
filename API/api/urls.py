from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('profils', views.ProfilViewSet)
router.register('strangethings', views.StrangethingViewSet)
router.register('likes', views.LikeViewSet)
router.register('comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]