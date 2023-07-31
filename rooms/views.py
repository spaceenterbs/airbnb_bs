# views는 유저가 특정 url에 접근했을 때 작동하게 되는 함수다.
# 예를 들어 유저가 /rooms에 접근했을 때 안녕이라고 말하고 싶다면, '안녕'이라고 말해줄 함수가 바로 views.py 안에 작성될 것이다.
"""
config의 urls.py를 import 해서 사용하므로,
views.py 파일의 이름은 꼭 view가 아니어도 된다. functions, controllers 등등으로 바꿔도 된다.
models.py와 apps.py, admin.py는 바꾸면 안된다.
"""
from django.shortcuts import render
from django.http import HttpResponse


# def say_hello(
#     request,
# ):  # 함수를 만들고 request object를 받을 공간을 만들어주는 것이 중요하다.
#     # request object는 요청하고 있는 브라우저의 정보, 전송하고 있는 데이터, 요청한  url정보, ip 주소, 쿠키 등 모든 정보를 갖고 있다.
#     # 장고는 또한 이 url에 요청을 보내고 있는 유저의 정보도 자동으로 request object 안에 넣어준다.
#     """request object는 유저가 보내는 데이터, 유저가 인증됐는지, 유저가 누군지 등 다양한 정보를 포함하고 있다."""
#     return HttpResponse("hello")  # "hello"  # 여기서는 일반 string을 리턴하고 있기에 에러가 발생한다.


"""우리가 url에서 변수를 받을거라고 장고에게 말하려면 어떻게 해야할까?"""


def see_all_rooms(request):
    # rooms = Room.objects.all()
    return HttpResponse("see all rooms")


def see_one_room(request, room_id):
    # def see_one_room(request, room_id, room_name): # rooms urls.py에서 <str:room_name>을 받으면 room_name도 추가해 줘야 한다. # room_id를 받을 자리를 만들어준다.
    return HttpResponse(f"see room with id: {room_id}")
