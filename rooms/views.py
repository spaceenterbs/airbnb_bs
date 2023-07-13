from django.shortcuts import render
from django.http import HttpResponse

# from .models import Room


def see_all_rooms(request):  # object request를 무지성으로 받는다.
    # rooms = Room.objects.all()
    return HttpResponse("see all rooms")


def see_one_room(request, room_id):  # room_name도 받을 수 있다.
    return HttpResponse(f"see room with idL {room_id}")
