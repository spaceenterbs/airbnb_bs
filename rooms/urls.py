from django.urls import path
from . import views

urlpatterns = [
    # path("", views.say_hello),  # 이 url은 이미 /rooms url로 들어온 url이기 때문에 ""(빈 문자열)을 넣어준다.
    # # config에서 옮겨진 것은, rooms url 선언의 위치를 바꾼 것 뿐이다.
    path(
        "", views.see_all_rooms
    ),  # rooms/ url을 받는다. "" 안에 hello를 넣으면 rooms/hello url을 받는다.
    path("<int:room_pk>", views.see_one_room),
    #     "<int:room_id>/<str:room_name>", views.see_one_room
    # ),  # <> 사이에 우리가 받을 parameter의 타입을 적어주고 매개변수의 이름도 적어준다.  # <int:room_id>/<str:room_name>같이 받을 수도 있다.
    # path("<str:room_name>", views.see_one_room), # 문자열을 받을 수도 있다.
]
