from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

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


class UrlsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.theatre_hall = TheatreHall.objects.create(
            name="Hall 1", rows=10, seats_in_row=20
        )
        self.play = Play.objects.create(
            title="Play 1", description="Description 1"
        )
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time="2024-08-20T20:00:00Z",
        )
        self.actor = Actor.objects.create(first_name="Actor", last_name="One")
        self.genre = Genre.objects.create(name="Genre 1")
        self.reservation = Reservation.objects.create(
            created_at="2024-08-20T20:00:00Z", user=self.user
        )
        self.ticket = Ticket.objects.create(
            row=1,
            seat=1,
            performance=self.performance,
            reservation=self.reservation,
        )

    def test_theatre_hall_url(self):
        response = self.client.get(reverse("theatre:theatre_halls-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_play_url(self):
        response = self.client.get(reverse("theatre:plays-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_url(self):
        response = self.client.get(reverse("theatre:performances-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actor_url(self):
        response = self.client.get(reverse("theatre:actors-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_genre_url(self):
        response = self.client.get(reverse("theatre:genres-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reservation_url(self):
        response = self.client.get(reverse("theatre:reservations-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_url(self):
        response = self.client.get(reverse("theatre:tickets-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_theatre_hall_detail_url(self):
        response = self.client.get(
            reverse(
                "theatre:theatre_halls-detail",
                kwargs={"pk": self.theatre_hall.pk},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_play_detail_url(self):
        response = self.client.get(
            reverse("theatre:plays-detail", kwargs={"pk": self.play.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_detail_url(self):
        response = self.client.get(
            reverse(
                "theatre:performances-detail",
                kwargs={"pk": self.performance.pk},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actor_detail_url(self):
        response = self.client.get(
            reverse("theatre:actors-detail", kwargs={"pk": self.actor.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_genre_detail_url(self):
        response = self.client.get(
            reverse("theatre:genres-detail", kwargs={"pk": self.genre.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reservation_detail_url(self):
        response = self.client.get(
            reverse(
                "theatre:reservations-detail",
                kwargs={"pk": self.reservation.pk},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_detail_url(self):
        response = self.client.get(
            reverse("theatre:tickets-detail", kwargs={"pk": self.ticket.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
