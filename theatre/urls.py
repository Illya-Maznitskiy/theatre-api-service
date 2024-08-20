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


router = routers.DefaultRouter()
router.register("theatre", TheatreHallViewSet, basename="theatre_hall")
router.register("play", PlayViewSet)
router.register("performance", PerformanceViewSet)
router.register("actor", ActorViewSet)
router.register("genre", GenreViewSet)
router.register("reservation", ReservationViewSet)
router.register("ticket", TicketViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
