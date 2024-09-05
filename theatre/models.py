from django.conf import settings
from django.db import models


class TheatreHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.rows} rows, {self.seats_in_row} seats/row"


class Play(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"Play: {self.title}"


class Performance(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    theatre_hall = models.ForeignKey(TheatreHall, on_delete=models.CASCADE)
    show_time = models.DateTimeField()

    def __str__(self):
        return (
            f"{self.play.title} at {self.theatre_hall.name} "
            f"on {self.show_time.strftime('%Y-%m-%d %H:%M')}"
        )


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Genre: {self.name}"


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            f"Reservation: {self.id} "
            f"on {self.created_at.strftime('%Y-%m-%d %H:%M')} "
            f"by {self.user.username}"
        )


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Ticket {self.row}-{self.seat} for "
            f"{self.performance.play.title} on "
            f"{self.performance.show_time.strftime('%Y-%m-%d %H:%M')}"
        )
