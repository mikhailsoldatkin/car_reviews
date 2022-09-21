from rest_framework.serializers import ModelSerializer

from .models import Country, Manufacturer, Car, Comment


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
