import json

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
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


class PublicTheatreHallTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_authentication_required(self):
        response = self.client.get(reverse("theatre:theatre_hall-list"))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateTheatreHallTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="user", password="password"
        )
        self.client.force_login(self.user)
        self.theatre_hall_list_url = reverse("theatre:theatre_hall-list")
        self.theatre_hall_detail_url = reverse(
            "theatre:theatre_hall-detail", kwargs={"pk": 1}
        )
        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=15
        )

    def test_retrieve_theatre_hall_detail(self):
        response = self.client.get(self.theatre_hall_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_theatre_hall(self):
        data = {"name": "Small Hall", "rows": 5, "seats_in_row": 8}
        response = self.client.post(
            self.theatre_hall_list_url, data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_theatre_hall_detail(self):
        data = {"name": "Updated Hall", "rows": 12, "seats_in_row": 16}
        response = self.client.put(
            self.theatre_hall_detail_url, data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_theatre_hall_detail(self):
        response = self.client.delete(self.theatre_hall_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicPlayTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_authentication_required(self):
        response = self.client.get(reverse("theatre:play-list"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivatePlayTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="user", password="password"
        )
        self.client.force_login(self.user)
        self.play_list_url = reverse("theatre:play-list")
        self.play_detail_url = reverse("theatre:play-detail", kwargs={"pk": 1})
        self.play = Play.objects.create(
            title="Hamlet", description="A tragedy by William Shakespeare"
        )

    def test_retrieve_play_detail(self):
        response = self.client.get(self.play_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_play(self):
        data = {
            "title": "Othello",
            "description": "A tragedy by William Shakespeare"
        }
        response = self.client.post(
            self.play_list_url, data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_play_detail(self):
        data = {
            "title": "Updated Hamlet", "description": "Updated description"
        }
        response = self.client.put(
            self.play_detail_url, data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_play_detail(self):
        response = self.client.delete(self.play_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicPerformanceTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_authentication_required(self):
        response = self.client.get(reverse("theatre:performance-list"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivatePerformanceTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="user", password="password"
        )
        self.client.force_login(self.user)

        self.play = Play.objects.create(
            title="Hamlet", description="A tragedy by William Shakespeare"
        )
        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=15
        )
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time=timezone.now()
        )

        self.performance_list_url = reverse("theatre:performance-list")
        self.performance_detail_url = reverse(
            "theatre:performance-detail",
            kwargs={"pk": self.performance.pk}
        )

    def test_retrieve_performance_detail(self):
        response = self.client.get(self.performance_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_performance(self):
        data = {
            "play": self.play.id,
            "theatre_hall": self.theatre_hall.id,
            "show_time": "2024-08-21 19:00:00"
        }
        response = self.client.post(
            self.performance_list_url, data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_performance_detail(self):
        data = {
            "play": self.play.id,
            "theatre_hall": self.theatre_hall.id,
            "show_time": "2024-08-21 20:00:00"
        }
        response = self.client.put(
            self.performance_detail_url, data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_performance_detail(self):
        response = self.client.delete(self.performance_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicActorTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_authentication_required(self):
        response = self.client.get(reverse("theatre:actor-list"))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateActorTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="user", password="password"
        )
        self.client.force_login(self.user)
        self.actor_list_url = reverse("theatre:actor-list")
        self.actor_detail_url = reverse(
            "theatre:actor-detail", kwargs={"pk": 1}
        )
        self.actor = Actor.objects.create(
            first_name="John", last_name="Doe"
        )

    def test_retrieve_actor_list(self):
        response = self.client.get(self.actor_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_actor(self):
        data = {"first_name": "Jane", "last_name": "Smith"}
        response = self.client.post(
            self.actor_list_url, data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_actor_detail(self):
        data = {"first_name": "Johnny", "last_name": "Doe"}
        response = self.client.put(
            self.actor_detail_url, data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_actor_detail(self):
        response = self.client.delete(self.actor_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicGenreTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_authentication_required(self):
        response = self.client.get(reverse("theatre:genre-list"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateGenreTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="user", password="password"
        )
        self.client.force_login(self.user)
        self.genre_list_url = reverse("theatre:genre-list")
        self.genre_detail_url = reverse("theatre:genre-detail", kwargs={"pk": 1})
        self.genre = Genre.objects.create(
            name="Drama"
        )

    def test_retrieve_genre_list(self):
        response = self.client.get(self.genre_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_genre(self):
        data = {"name": "Comedy"}
        response = self.client.post(
            self.genre_list_url, data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_genre_detail(self):
        data = {"name": "Updated Drama"}
        response = self.client.put(
            self.genre_detail_url, data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_genre_detail(self):
        response = self.client.delete(self.genre_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicReservationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_authentication_required(self):
        response = self.client.get(reverse("theatre:reservation-list"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateReservationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="uniqueuser", email="some_user@example.com", password="testpass"
        )
        self.client.force_login(self.user)

        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=10
        )
        self.play = Play.objects.create(
            title="Hamlet", description="A Shakespearean tragedy"
        )
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time=timezone.now()
        )
        self.reservation_list_url = reverse("theatre:reservation-list")
        self.reservation_detail_url = reverse(
            "theatre:reservation-detail", kwargs={"pk": 1}
        )
        self.reservation = Reservation.objects.create(user=self.user)

    def test_retrieve_reservation_list(self):
        response = self.client.get(self.reservation_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_reservation(self):
        data = {
            "user": self.user.id
        }
        response = self.client.post(
            self.reservation_list_url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_reservation_detail(self):
        data = {"user": self.user.id}
        response = self.client.put(
            self.reservation_detail_url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_reservation_detail(self):
        response = self.client.delete(self.reservation_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicTicketTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_authentication_required(self):
        response = self.client.get(reverse("theatre:ticket-list"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateTicketTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="user", password="password"
        )
        self.client.force_login(self.user)

        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=15
        )
        self.play = Play.objects.create(
            title="Hamlet", description="A tragedy by William Shakespeare"
        )
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time=timezone.now()
        )
        self.reservation = Reservation.objects.create(user=self.user)
        self.ticket_list_url = reverse("theatre:ticket-list")
        self.ticket_detail_url = reverse("theatre:ticket-detail", kwargs={"pk": 1})
        self.ticket = Ticket.objects.create(
            row=1,
            seat=1,
            performance=self.performance,
            reservation=self.reservation
        )

    def test_retrieve_ticket_detail(self):
        response = self.client.get(self.ticket_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_ticket(self):
        data = {
            "row": 2,
            "seat": 2,
            "performance": self.performance.id,
            "reservation": self.reservation.id
        }
        response = self.client.post(
            self.ticket_list_url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_ticket_detail(self):
        data = {
            "row": 3,
            "seat": 3,
            "performance": self.performance.id,
            "reservation": self.reservation.id
        }
        response = self.client.put(
            self.ticket_detail_url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_ticket_detail(self):
        response = self.client.delete(self.ticket_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
