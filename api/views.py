from rest_framework.viewsets import ModelViewSet

from .models import Country
from .serializers import CountrySerializer, ManufacturerSerializer, \
    CarSerializer, CommentSerializer


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    # permission_classes = (IsAuthorOrReadOnly | IsAdminOrReadOnly,)


class ManufacturerViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = ManufacturerSerializer


class CarViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CarSerializer


class CommentViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CommentSerializer
