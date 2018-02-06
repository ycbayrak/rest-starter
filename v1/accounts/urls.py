from django.conf.urls import url, include
from .views.profile import ProfileView
from .views.user import UserView, UserViewSet
from .views.profile import ProfileView, ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'accounts', UserViewSet, base_name="account")

urlpatterns = [
    url(r'', include(router.urls))
]
