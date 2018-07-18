# Third-Party
from rest_framework import serializers

# Django
from django.conf import settings
#from django.core.serializers import serialize
from django.utils.translation import ugettext_lazy as _

# Local Django
from Users.models import User
from Park.models import Park
from Core.models import City
from Core.serializers import CitySerializer


class ParkSerializer(serializers.ModelSerializer):
    try:
        city = City.objects.get(user_id=id)
        serializer = CitySerializer(many=True, read_only=True)
    except:
        pass

    #serialize ( 'geojson' , Park.objects.all(),
          #geometry_field = 'point' ,
          #fields = ( 'coordinate' ,))

    create_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    #number_of_car_inside
    #coordinate
    class Meta:
        model = Park
        fields = ('id', 'city', 'name', 'address', 'capacity', 'number_of_car_inside', 'create_time', 'coordinate')

class ParkListSerializer(ParkSerializer):

    class Meta:
        model = Park
        fields = ('id', 'name', 'capacity', 'coordinate','number_of_car_inside',)


class ParkRetrieveSerializer(ParkSerializer):
    pass


class ParkCreateSerializer(ParkSerializer):

    class Meta:
        model = Park
        fields = ('city', 'name', 'address', 'capacity', 'coordinate', 'number_of_car_inside')


class ParkUpdateSerializer(ParkSerializer):
    #number_of_car_inside
    class Meta:
        model = Park
        fields = ('name', 'address', 'coordinate', 'capacity')
