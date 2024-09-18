from django.contrib import admin
from .models import (
    TheatreHall,
    Play,
    Performance,
    Actor,
    Genre,
    Reservation,
    Ticket,
)


@admin.register(TheatreHall)
class TheatreHallAdmin(admin.ModelAdmin):
    list_display = ("name", "rows", "seats_in_row")


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("play", "theatre_hall", "show_time")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("created_at", "user")


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("row", "seat", "performance", "reservation")
