import csv

from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, \
    AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .mixins import CustomViewSet
from .models import Country, Manufacturer, Car, Comment
from .serializers import (
    CountrySerializer, ManufacturerSerializer, CarSerializer,
    CommentReadSerializer, CommentWriteSerializer
)


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ManufacturerViewSet(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return CommentReadSerializer
        return CommentWriteSerializer

    def get_permissions(self):
        if self.request.method in ('GET', 'POST'):
            return [AllowAny()]
        elif self.request.method in ('PUT', 'DELETE'):
            return [IsAuthenticated()]


def export_data(request):
    model = Car
    parameter = request.GET.get('parameter')
    filename = f'{model._meta.model_name}.{parameter}'

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    field_names = [field.name for field in model._meta.fields]

    writer = csv.writer(response)
    writer.writerow(field_names)

    objects = model.objects.all().values_list(*field_names)
    for obj in objects:
        writer.writerow(obj)

    return response
