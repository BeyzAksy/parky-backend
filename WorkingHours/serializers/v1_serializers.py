# Local Django
from .base_serializers import (
    WorkingHoursSerializer, WorkingHoursListSerializer,
    WorkingHoursRetrieveSerializer, WorkingHoursUpdateSerializer,
)


class WorkingHoursSerializerV1(WorkingHoursSerializer):
    pass


class WorkingHoursListSerializerV1(WorkingHoursListSerializer):
    pass


class WorkingHoursRetrieveSerializerV1(WorkingHoursRetrieveSerializer):
    pass


class WorkingHoursUpdateSerializerV1(WorkingHoursUpdateSerializer):
    pass
