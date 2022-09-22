from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
)

from .mixins import CustomViewSet
from .models import Country, Manufacturer, Car, Comment
from .serializers import (
    CountrySerializer, ManufacturerSerializer, CommentSerializer,
    CarSerializer
)


class CountryViewSet(CustomViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ManufacturerViewSet(CustomViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CarViewSet(CustomViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSet(CustomViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method in ('GET', 'POST'):
            return [AllowAny()]
        elif self.request.method in ('PUT', 'DELETE'):
            return [IsAuthenticated()]
