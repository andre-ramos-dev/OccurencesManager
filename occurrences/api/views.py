from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from occurrences.api.serializers import OccurrenceSerializer
from occurrences.filters import OccurrenceFilter
from occurrences.models import Occurrence


class OccurrenceViewSet(viewsets.ModelViewSet):
    """
     This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OccurrenceFilter

    def get_queryset(self):
        occurrences = super().get_queryset()
        lng = self.request.query_params.get('lng', None)
        lat = self.request.query_params.get('lat', None)
        radius = self.request.query_params.get('radius', None)
        if lat and lng and radius:
            occurrences = occurrences.filter(
                location__distance_lte=(Point(float(lng), float(lat)), Distance(km=radius)))

        return occurrences

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_update(self, serializer):
        serializer.update(self.get_object(), serializer.validated_data)
