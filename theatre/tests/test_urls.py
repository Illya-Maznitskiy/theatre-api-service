from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from theatre.models import (
    TheatreHall,
    Play,
    Performance,
    Actor,
    Genre,
    Reservation,
    Ticket,
)


class UrlsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

        # Create test data
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
        response = self.client.get(reverse("theatre:theatre_hall-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_play_url(self):
        response = self.client.get(reverse("theatre:play-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_url(self):
        response = self.client.get(reverse("theatre:performance-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actor_url(self):
        response = self.client.get(reverse("theatre:actor-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_genre_url(self):
        response = self.client.get(reverse("theatre:genre-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reservation_url(self):
        response = self.client.get(reverse("theatre:reservation-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_url(self):
        response = self.client.get(reverse("theatre:ticket-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_theatre_hall_detail_url(self):
        response = self.client.get(
            reverse(
                "theatre:theatre_hall-detail",
                kwargs={"pk": self.theatre_hall.pk},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_play_detail_url(self):
        response = self.client.get(
            reverse("theatre:play-detail", kwargs={"pk": self.play.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_detail_url(self):
        response = self.client.get(
            reverse(
                "theatre:performance-detail",
                kwargs={"pk": self.performance.pk},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actor_detail_url(self):
        response = self.client.get(
            reverse("theatre:actor-detail", kwargs={"pk": self.actor.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_genre_detail_url(self):
        response = self.client.get(
            reverse("theatre:genre-detail", kwargs={"pk": self.genre.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reservation_detail_url(self):
        response = self.client.get(
            reverse(
                "theatre:reservation-detail",
                kwargs={"pk": self.reservation.pk},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_detail_url(self):
        response = self.client.get(
            reverse("theatre:ticket-detail", kwargs={"pk": self.ticket.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
