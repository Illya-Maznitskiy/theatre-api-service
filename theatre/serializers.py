from rest_framework import serializers
from django.contrib.auth import get_user_model

from theatre.models import (
    TheatreHall,
    Play,
    Performance,
    Actor,
    Genre,
    Reservation,
    Ticket,
)


User = get_user_model()


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ("id", "name", "rows", "seats_in_row")


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ("id", "title", "description")


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ("id", "play", "theatre_hall", "show_time")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )
    created_at = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M:%S%z", read_only=True
    )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        created_at = instance.created_at
        representation["created_at"] = (
            created_at.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        )
        return representation

    class Meta:
        model = Reservation
        fields = ("id", "created_at", "user")


class TicketSerializer(serializers.ModelSerializer):
    performance = serializers.PrimaryKeyRelatedField(
        queryset=Performance.objects.all()
    )
    reservation = serializers.PrimaryKeyRelatedField(
        queryset=Reservation.objects.all()
    )

    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "performance", "reservation")
