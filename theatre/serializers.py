from rest_framework import serializers
from django.contrib.auth.models import User

from theatre.models import (
    TheatreHall,
    Play,
    Performance,
    Actor,
    Genre,
    Reservation,
    Ticket
)


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ('id', 'name', "rows", "seats_in_row")


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
        fields = ('id', 'username', 'email')


class ReservationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Reservation
        fields = ("id", "created_at", "user")


class TicketSerializer(serializers.ModelSerializer):
    performance = PerformanceSerializer()
    reservation = ReservationSerializer()

    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "performance", "reservation")
