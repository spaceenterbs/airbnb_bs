from django.shortcuts import render
from django.http import HttpResponse


def see_all_rooms(request):  # object request를 무지성으로 받는다.
    return HttpResponse("see all rooms")


def see_one_room(request, room_id):
    return HttpResponse(f"see room with idL {room_id}")
