from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField
from rest_framework.serializers import ModelSerializer

from .models import Country, Manufacturer, Car, Comment


class CommentReadSerializer(ModelSerializer):
    car = SlugRelatedField(slug_field='name', queryset=Car.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'author_email', 'car', 'created', 'text')


class CommentWriteSerializer(ModelSerializer):
    car = SlugRelatedField(slug_field='name', queryset=Car.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'author_email', 'car', 'created', 'text')

    def validate_text(self, value):
        if Comment.objects.filter(text=value).exists():
            raise ValidationError('Вы уже писали такой комментарий!')
        return value


class CarSerializer(ModelSerializer):
    manufacturer = SlugRelatedField(slug_field='name',
                                    queryset=Manufacturer.objects.all())
    comments_count = SerializerMethodField()
    comments = CommentReadSerializer(many=True)

    class Meta:
        model = Car
        fields = (
            'id',
            'name',
            'manufacturer',
            'start_year',
            'end_year',
            'comments',
            'comments_count'
        )

    def get_comments_count(self, obj):
        return obj.comments.count()

    def validate_end_year(self, value):
        start_year = self.initial_data['start_year']
        if value >= start_year:
            return value


class ManufacturerSerializer(ModelSerializer):
    cars = SerializerMethodField()
    comments_count = SerializerMethodField()
    country = SlugRelatedField(slug_field='name',
                               queryset=Country.objects.all())

    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'country', 'cars', 'comments_count')

    def get_comments_count(self, obj):
        return Comment.objects.filter(car__manufacturer=obj).count()

    def get_cars(self, obj):
        return obj.cars.values('id', 'name')


class CountrySerializer(ModelSerializer):
    manufacturers = SerializerMethodField()

    class Meta:
        model = Country
        fields = ('id', 'name', 'manufacturers')

    def get_manufacturers(self, obj):
        return obj.manufacturers.values('id', 'name')
