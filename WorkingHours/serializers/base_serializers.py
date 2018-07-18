# Third-Party
from rest_framework import serializers

# Django
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Local Django
from Users.models import User
from WorkingHours.models import WorkingHours
from Park.models import Park
from Park.serializers import ParkSerializer

class WorkingHoursSerializer(serializers.ModelSerializer):
    try:
        park = Park.objects.get(user_id=id)
        serializer = ParkSerializer(many=True, read_only=True)
    except:
        pass

    tip = serializers.CharField(source='get_tip_display')
    start_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    end_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model = WorkingHours
        fields = ('id', 'park', 'type', 'start_time', 'end_time')


class WorkingHoursListSerializer(WorkingHoursSerializer):

    class Meta:
        model = WorkingHours
        fields = ('id', 'park', 'start_time', 'end_time')


class WorkingHoursRetrieveSerializer(WorkingHoursSerializer):
    pass

class WorkingHoursUpdateSerializer(WorkingHoursSerializer):

    class Meta:
        model = WorkingHours
        fields = ('start_time', 'end_time')
