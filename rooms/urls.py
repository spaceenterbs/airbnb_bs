from django.urls import path
from . import views

urlpatterns = [
    path(
        "", views.see_all_rooms
    ),  # rooms/ url을 받는다. "" 안에 hello를 넣으면 rooms/hello url을 받는다.
    path("<int:room_id>", views.see_one_room),
    # path("<str:room_name>", views.see_one_room), # 문자열을 받을 수도 있다.
]
