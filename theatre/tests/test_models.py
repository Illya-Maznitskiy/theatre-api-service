from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from theatre.models import (
    TheatreHall,
    Play,
    Performance,
    Actor,
    Genre,
    Reservation,
    Ticket,
)


user = get_user_model()


class TestTheatreModels(TestCase):
    def setUp(self):
        self.play = Play.objects.create(
            title="Hamlet",
            description="A tragedy by Shakespeare",
        )
        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=20
        )
        self.show_time = timezone.now() + timezone.timedelta(days=1)
        self.user = user.objects.create_user(
            username="testuser",
            password="password",
        )

    def test_create_theatre_hall(self):
        theatre_hall = self.theatre_hall
        self.assertEqual(theatre_hall.name, "Main Hall")
        self.assertEqual(theatre_hall.rows, 10)
        self.assertEqual(theatre_hall.seats_in_row, 20)
        self.assertEqual(
            str(theatre_hall), "Main Hall - 10 rows, 20 seats/row"
        )

    def test_create_play(self):
        play = self.play
        self.assertEqual(play.title, "Hamlet")
        self.assertEqual(play.description, "A tragedy by Shakespeare")
        self.assertEqual(str(play), "Play: Hamlet")

    def test_create_performance(self):
        performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time=self.show_time,
        )
        self.assertEqual(performance.play, self.play)
        self.assertEqual(performance.theatre_hall, self.theatre_hall)
        self.assertEqual(performance.show_time, self.show_time)
        self.assertEqual(
            str(performance),
            f"Hamlet at Main Hall on "
            f"{self.show_time.strftime('%Y-%m-%d %H:%M')}",
        )

    def test_create_actor(self):
        actor = Actor.objects.create(
            first_name="William",
            last_name="Shakespeare",
        )
        self.assertEqual(actor.first_name, "William")
        self.assertEqual(actor.last_name, "Shakespeare")
        self.assertEqual(str(actor), "William Shakespeare")

    def test_create_genre(self):
        genre = Genre.objects.create(
            name="Tragedy",
        )
        self.assertEqual(genre.name, "Tragedy")
        self.assertEqual(str(genre), "Genre: Tragedy")

    def test_create_reservation(self):
        reservation = Reservation.objects.create(
            user=self.user,
        )
        self.assertEqual(reservation.user, self.user)
        self.assertTrue(reservation.created_at)
        self.assertEqual(
            str(reservation),
            f"Reservation: {reservation.id} on "
            f"{reservation.created_at.strftime('%Y-%m-%d %H:%M')} "
            f"by {self.user.username}",
        )

    def test_create_ticket(self):
        performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time=self.show_time,
        )
        reservation = Reservation.objects.create(
            user=self.user,
        )
        ticket = Ticket.objects.create(
            row=5,
            seat=10,
            performance=performance,
            reservation=reservation,
        )
        self.assertEqual(ticket.row, 5)
        self.assertEqual(ticket.seat, 10)
        self.assertEqual(ticket.performance, performance)
        self.assertEqual(ticket.reservation, reservation)
        self.assertEqual(
            str(ticket),
            f"Ticket 5-10 for Hamlet on "
            f"{self.show_time.strftime('%Y-%m-%d %H:%M')}",
        )
