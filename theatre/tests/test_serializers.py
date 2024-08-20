from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from theatre.models import (
    TheatreHall,
    Play,
    Performance,
    Actor,
    Genre,
    Reservation,
    Ticket,
)
from theatre.serializers import (
    TheatreHallSerializer,
    PlaySerializer,
    PerformanceSerializer,
    ActorSerializer,
    GenreSerializer,
    ReservationSerializer,
    TicketSerializer,
)


class BaseSerializerTestCase(APITestCase):
    def assert_serialized_equal(self, serializer, instance, expected_data):
        """Helper method to test serialization"""
        serializer_instance = serializer(instance)
        self.assertEqual(serializer_instance.data, expected_data)


class TestSerializer(BaseSerializerTestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="user@example.com", password="testpass"
        )

        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=20
        )

        self.play = Play.objects.create(
            title="Hamlet", description="A Shakespearean play"
        )

        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time="2024-08-12T00:00:00Z",
        )

        self.actor = Actor.objects.create(first_name="John", last_name="Doe")

        self.genre = Genre.objects.create(name="Drama")

        self.reservation = Reservation.objects.create(
            user=self.user, created_at="2024-08-10T10:00:00Z"
        )

        self.ticket = Ticket.objects.create(
            row=5,
            seat=10,
            performance=self.performance,
            reservation=self.reservation,
        )

    def test_theatre_hall_serializer(self):
        expected_data = {
            "id": self.theatre_hall.id,
            "name": "Main Hall",
            "rows": 10,
            "seats_in_row": 20,
        }
        self.assert_serialized_equal(
            TheatreHallSerializer, self.theatre_hall, expected_data
        )

    def test_play_serializer(self):
        expected_data = {
            "id": self.play.id,
            "title": "Hamlet",
            "description": "A Shakespearean play",
        }
        self.assert_serialized_equal(PlaySerializer, self.play, expected_data)

    def test_performance_serializer(self):
        expected_data = {
            "id": self.performance.id,
            "play": self.play.id,
            "theatre_hall": self.theatre_hall.id,
            "show_time": "2024-08-12T00:00:00Z",
        }
        self.assert_serialized_equal(
            PerformanceSerializer, self.performance, expected_data
        )

    def test_actor_serializer(self):
        expected_data = {
            "id": self.actor.id,
            "first_name": "John",
            "last_name": "Doe",
        }
        self.assert_serialized_equal(
            ActorSerializer, self.actor, expected_data
        )

    def test_genre_serializer(self):
        expected_data = {
            "id": self.genre.id,
            "name": "Drama",
        }
        self.assert_serialized_equal(
            GenreSerializer, self.genre, expected_data
        )

    def test_reservation_serializer(self):
        expected_data = {
            "id": self.reservation.id,
            "created_at": self.reservation.created_at.strftime(
                "%Y-%m-%dT%H:%M:%S"
            )
                          + "Z",
            "user": self.user.id,
        }
        self.assert_serialized_equal(
            ReservationSerializer, self.reservation, expected_data
        )

    def test_ticket_serializer(self):
        expected_data = {
            "id": self.ticket.id,
            "row": 5,
            "seat": 10,
            "performance": self.performance.id,
            "reservation": self.reservation.id,
        }
        self.assert_serialized_equal(
            TicketSerializer, self.ticket, expected_data
        )
