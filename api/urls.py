from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CountryViewSet, ManufacturerViewSet, CarViewSet, CommentViewSet
)

app_name = 'api'

router = DefaultRouter()

router.register('countries', CountryViewSet)
router.register('manufacturers', ManufacturerViewSet)
router.register('cars', CarViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]