import csv

from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet


class CustomViewSet(ListModelMixin, CreateModelMixin,
                    DestroyModelMixin, UpdateModelMixin,
                    GenericViewSet):

    def export_data(self, request):
        parameter = request.GET.get('parameter')
        model = self.queryset.model
        object_list = model.objects.all()

        meta = model._meta
        field_names = [field.name for field in meta.fields]
        filename = f'{meta}.{parameter}'

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={filename}'

        writer = csv.writer(response)
        writer.writerow(field_names)

        objects = object_list.values_list(field_names)
        for obj in objects:
            writer.writerow(obj)

        return response
