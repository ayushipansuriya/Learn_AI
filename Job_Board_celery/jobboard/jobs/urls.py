from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, SubscriberViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'subscribers', SubscriberViewSet)

urlpatterns = router.urls
