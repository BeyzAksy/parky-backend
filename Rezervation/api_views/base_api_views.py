# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from Rezervation.models import Rezervation
from Users.models import User
from Rezervation.serializers import (
    RezervationSerializer, RezervationListSerializer, RezervationCreateSerializer,
    RezervationRetrieveSerializer, RezervationUpdateSerializer
)


class RezervationViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Rezervation.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.id)

    def get_serializer_class(self):
        if self.action == 'list':
            return RezervationListSerializer
        elif self.action == 'create':
            return RezervationCreateSerializer
        elif self.action == 'retrieve':
            return RezervationRetrieveSerializer
        elif self.action == 'update':
            return RezervationUpdateSerializer
        else:
            return RezervationSerializer

    def get_permissions(self):
        permissions = super(RezervationViewSet, self).get_permissions()

        if self.action in ['list', 'retrieve', 'delete',]:     #Böyle mi olmalı???
            return []

        return permissions

    def perform_create(self, serializer):
        rezervation = serializer.save(user=self.request.user)
        rezervation.save()

    def perform_destroy(self, instance):

        super(RezervationViewSet, self).perform_destroy(instance)
