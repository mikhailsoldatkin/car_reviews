import csv

import xlsxwriter
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin,
    RetrieveModelMixin
)
from rest_framework.viewsets import GenericViewSet


class CustomViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                    DestroyModelMixin, UpdateModelMixin,
                    GenericViewSet):

    @action(
        detail=False,
        url_path='export-data'
    )
    def export_data(self, request):
        model = self.queryset.model
        parameter = request.GET.get('parameter')
        filename = f'{model._meta.model_name}.{parameter}'
        field_names = [field.name for field in model._meta.fields]

        if parameter == 'csv':

            response = HttpResponse(content_type='text/csv')
            response[
                'Content-Disposition'] = f'attachment; filename={filename}'

            writer = csv.writer(response)
            writer.writerow(field_names)

            objects = model.objects.all().values_list(*field_names)
            for obj in objects:
                writer.writerow(obj)

            return response

        if parameter == 'xlsx':

            response = HttpResponse(content_type='application/vnd.ms-excel')
            response[
                'Content-Disposition'] = f'attachment; filename={filename}'

            workbook = xlsxwriter.Workbook(response)
            worksheet = workbook.add_worksheet(f'{model._meta.model_name}')

            row_num = 0
            columns = field_names
            for col_num in range(len(columns)):
                worksheet.write(row_num, col_num, columns[col_num])

            rows = model.objects.all().values_list(*field_names)
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    worksheet.write(row_num, col_num, row[col_num])

            workbook.close()

            return response
