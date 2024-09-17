from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
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


class PublicTheatreHallTest(APITestCase):

    def test_authentication_required(self):
        response = self.client.post(reverse("theatre:theatre_halls-list"))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTheatreHallTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=15
        )
        self.theatre_halls_list_url = reverse("theatre:theatre_halls-list")
        self.theatre_halls_detail_url = reverse(
            "theatre:theatre_halls-detail", kwargs={"pk": self.theatre_hall.pk}
        )

    def test_retrieve_theatre_hall_detail(self):
        response = self.client.get(self.theatre_halls_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_theatre_hall(self):
        data = {"name": "Small Hall", "rows": 5, "seats_in_row": 8}
        response = self.client.post(
            self.theatre_halls_list_url,
            data=data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_theatre_hall_detail(self):
        data = {"name": "Updated Hall", "rows": 12, "seats_in_row": 16}
        response = self.client.put(
            self.theatre_halls_detail_url,
            data=data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_theatre_hall_detail(self):
        response = self.client.delete(self.theatre_halls_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicPlayTest(APITestCase):

    def test_authentication_required(self):
        response = self.client.post("/api/theatre/theatre-halls/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivatePlayTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.play = Play.objects.create(
            title="Hamlet", description="A tragedy by William Shakespeare"
        )
        self.plays_list_url = reverse("theatre:plays-list")
        self.plays_detail_url = reverse(
            "theatre:plays-detail", kwargs={"pk": self.play.pk}
        )

    def test_retrieve_play_detail(self):
        response = self.client.get(self.plays_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_play(self):
        data = {
            "title": "Othello",
            "description": "A tragedy by William Shakespeare",
        }
        response = self.client.post(self.plays_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_play_detail(self):
        data = {
            "title": "Updated Hamlet",
            "description": "Updated description",
        }
        response = self.client.put(
            self.plays_detail_url, data=data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_play_detail(self):
        response = self.client.delete(self.plays_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicPerformanceTest(APITestCase):

    def test_authentication_required(self):
        response = self.client.post(reverse("theatre:performances-list"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivatePerformanceTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.play = Play.objects.create(
            title="Hamlet", description="A tragedy by William Shakespeare"
        )
        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=15
        )
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time=timezone.now(),
        )

        self.performances_list_url = reverse("theatre:performances-list")
        self.performances_detail_url = reverse(
            "theatre:performances-detail", kwargs={"pk": self.performance.pk}
        )

    def test_retrieve_performance_detail(self):
        response = self.client.get(self.performances_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_performance(self):
        data = {
            "play": self.play.id,
            "theatre_hall": self.theatre_hall.id,
            "show_time": "2024-08-21 19:00:00",
        }
        response = self.client.post(
            self.performances_list_url, data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_performance_detail(self):
        data = {
            "play": self.play.id,
            "theatre_hall": self.theatre_hall.id,
            "show_time": "2024-08-21 20:00:00",
        }
        response = self.client.put(
            self.performances_detail_url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_performance_detail(self):
        response = self.client.delete(self.performances_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicActorTest(APITestCase):
    def test_authentication_required(self):
        response = self.client.post(reverse("theatre:actors-list"))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateActorTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.actor = Actor.objects.create(first_name="John", last_name="Doe")
        self.actors_list_url = reverse("theatre:actors-list")
        self.actors_detail_url = reverse(
            "theatre:actors-detail", kwargs={"pk": self.actor.pk}
        )

    def test_retrieve_actor_list(self):
        response = self.client.get(self.actors_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_actor(self):
        data = {"first_name": "Jane", "last_name": "Smith"}
        response = self.client.post(self.actors_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_actor_detail(self):
        data = {"first_name": "Johnny", "last_name": "Doe"}
        response = self.client.put(self.actors_detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_actor_detail(self):
        response = self.client.delete(self.actors_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicGenreTest(APITestCase):
    def test_authentication_required(self):
        response = self.client.post(reverse("theatre:genres-list"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateGenreTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.genre = Genre.objects.create(name="Drama")
        self.genres_list_url = reverse("theatre:genres-list")
        self.genres_detail_url = reverse(
            "theatre:genres-detail", kwargs={"pk": self.genre.pk}
        )

    def test_retrieve_genre_list(self):
        response = self.client.get(self.genres_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_genre(self):
        data = {"name": "Comedy"}
        response = self.client.post(self.genres_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_genre_detail(self):
        data = {"name": "Updated Drama"}
        response = self.client.put(self.genres_detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_genre_detail(self):
        response = self.client.delete(self.genres_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicReservationTest(APITestCase):
    def test_authentication_required(self):
        response = self.client.post(reverse("theatre:reservations-list"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateReservationTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=10
        )
        self.play = Play.objects.create(
            title="Hamlet", description="A Shakespearean tragedy"
        )
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time=timezone.now(),
        )
        self.reservation = Reservation.objects.create(user=self.user)
        self.reservations_list_url = reverse("theatre:reservations-list")
        self.reservations_detail_url = reverse(
            "theatre:reservations-detail",
            kwargs={"pk": self.reservation.pk},  # Use self.reservation.pk here
        )

    def test_retrieve_reservation_list(self):
        response = self.client.get(self.reservations_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_reservation(self):
        data = {"user": self.user.id}
        response = self.client.post(
            self.reservations_list_url, data=data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_reservation_detail(self):
        data = {"user": self.user.id}
        response = self.client.put(
            self.reservations_detail_url, data=data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_reservation_detail(self):
        response = self.client.delete(self.reservations_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicTicketTest(APITestCase):
    def test_authentication_required(self):
        response = self.client.post(reverse("theatre:tickets-list"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTicketTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=15
        )
        self.play = Play.objects.create(
            title="Hamlet", description="A tragedy by William Shakespeare"
        )
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time=timezone.now(),
        )
        self.reservation = Reservation.objects.create(user=self.user)
        self.ticket = Ticket.objects.create(
            row=1,
            seat=1,
            performance=self.performance,
            reservation=self.reservation,
        )
        self.tickets_list_url = reverse("theatre:tickets-list")
        self.tickets_detail_url = reverse(
            "theatre:tickets-detail",
            kwargs={"pk": self.ticket.pk},  # Use self.ticket.pk here
        )

    def test_retrieve_ticket_detail(self):
        response = self.client.get(self.tickets_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_ticket(self):
        data = {
            "row": 2,
            "seat": 2,
            "performance": self.performance.id,
            "reservation": self.reservation.id,
        }
        response = self.client.post(
            self.tickets_list_url, data=data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_ticket_detail(self):
        data = {
            "row": 3,
            "seat": 3,
            "performance": self.performance.id,
            "reservation": self.reservation.id,
        }
        response = self.client.put(
            self.tickets_detail_url, data=data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_ticket_detail(self):
        response = self.client.delete(self.tickets_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
