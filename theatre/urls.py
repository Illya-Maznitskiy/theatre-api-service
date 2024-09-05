from django.urls import path, include
from rest_framework import routers

from theatre.views import (
    TheatreHallViewSet,
    PlayViewSet,
    PerformanceViewSet,
    ActorViewSet,
    GenreViewSet,
    ReservationViewSet,
    TicketViewSet,
)


router = routers.SimpleRouter()
router.register(
    "theatre-halls", TheatreHallViewSet, basename="theatre_halls"
)
router.register("plays", PlayViewSet, basename="plays")
router.register("performances", PerformanceViewSet, basename="performances")
router.register("actors", ActorViewSet, basename="actors")
router.register("genres", GenreViewSet, basename="genres")
router.register("reservations", ReservationViewSet, basename="reservations")
router.register("tickets", TicketViewSet, basename="tickets")

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
