from rest_framework import viewsets, permissions

from theatre.models import (
    TheatreHall,
    Play,
    Performance,
    Actor,
    Genre,
    Reservation,
    Ticket
)
from theatre.serializers import (
    TheatreHallSerializer,
    PlaySerializer,
    PerformanceSerializer,
    ActorSerializer,
    GenreSerializer,
    ReservationSerializer,
    TicketSerializer
)


class StaffRequiredPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [StaffRequiredPermission]


class TheatreHallViewSet(BaseViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer


class PlayViewSet(BaseViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer


class PerformanceViewSet(BaseViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer


class ActorViewSet(BaseViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(BaseViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReservationViewSet(BaseViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TicketViewSet(BaseViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
