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
router.register("plays", PlayViewSet)
router.register("performances", PerformanceViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("reservations", ReservationViewSet)
router.register("tickets", TicketViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
