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

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
