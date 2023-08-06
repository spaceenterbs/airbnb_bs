from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Amenity
from .serializers import AmenitySerializer  # 어떤 폴더에서 어떤 클래스를 가져온다.

# /api/v1/rooms/amenities, /api/v1/rooms/amenities/1


class Amenities(
    APIView
):  # request method가 GET인지, POST인지 확인하는 조건문 코드를 쓰지 않아도 되기에 APIView를 쓴다.
    def get(self, request):
        all_amenities = Amenity.objects.all()  # 모든 amenity를 본다.
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(
            data=request.data
        )  # 사용자의 데이터로 serializer를 만들 때는, serializer는 사용자의 데이터가 amenity object가 원하는 데이터에 준수하는지 검증해야 한다.
        if serializer.is_valid():
            amenity = (  # serializer를 save하고 나면, serializer는 새로운 amenity를 만든다. 그리고 그 amenity를 return한다.
                serializer.save()
            )  # serializer.save() 해서 ModelSerializer가 자동으로 amenity를 만들게 한다.
            return Response(
                AmenitySerializer(amenity).data,  # 그러면 새로 만들어진 amenity를 return한다.
            )
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound  # amenity를 찾아서 반환하거나 찾지 못할 경우 NotFound를 반환하는 method를 만든것.

    def get(self, request, pk):  # amenities/<int:pk>로 우리가 URL에 요청했기에 pk가 필요하다.
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)
        # return Response(
        #     AmenitySerializer(
        #         self.get_object(pk),
        #     ).data,
        # )

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(
            amenity,  # 데이터베이스에 있는, 업데이트하고싶은 amenity
            data=request.data,  # 사용자가 보낸 데이터. 따라서 위와 아래의 두 데이터로 serializer를 만든다.
            partial=True,
        )  # partial=True를 넣어주면, 모든 필드를 채울 필요가 없다. name이나 description만(둘 다는 X) 변경할 수 있게 한다.
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(
                AmenitySerializer(updated_amenity).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    # views는 유저가 특정 url에 접근했을 때 작동하게 되는 함수다.
    # 예를 들어 유저가 /rooms에 접근했을 때 안녕이라고 말하고 싶다면, '안녕'이라고 말해줄 함수가 바로 views.py 안에 작성될 것이다.

    """config의 urls.py를 import 해서 사용하므로,
    views.py 파일의 이름은 꼭 view가 아니어도 된다. functions, controllers 등등으로 바꿔도 된다.
    models.py와 apps.py, admin.py는 바꾸면 안된다."""


# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Room


# # def say_hello(
# #     request,
# # ):  # 함수를 만들고 request object를 받을 공간을 만들어주는 것이 중요하다.
# #     # request object는 요청하고 있는 브라우저의 정보, 전송하고 있는 데이터, 요청한  url정보, ip 주소, 쿠키 등 모든 정보를 갖고 있다.
# #     # 장고는 또한 이 url에 요청을 보내고 있는 유저의 정보도 자동으로 request object 안에 넣어준다.
# #     """request object는 유저가 보내는 데이터, 유저가 인증됐는지, 유저가 누군지 등 다양한 정보를 포함하고 있다."""
# #     return HttpResponse("hello")  # "hello"  # 여기서는 일반 string을 리턴하고 있기에 에러가 발생한다.


# """우리가 url에서 변수를 받을거라고 장고에게 말하려면 어떻게 해야할까?"""


# def see_all_rooms(request):
#     rooms = Room.objects.all()  # rencer 1. DB에 있는 모든 방의 정보를 받아온다.
#     # return HttpResponse("see all rooms")
#     return render(
#         request,
#         "all_rooms.html",
#         {"rooms": rooms, "title": "Hello! this title comes from django!"},
#     )  # all_rooms라는 템플릿을 렌더링하며 rooms와 title을 넘겨준다. #유저에게 HTML을 렌더링 해준다.


# def see_one_room(request, room_pk):
#     # def see_one_room(request, room_id, room_name): # rooms urls.py에서 <str:room_name>을 받으면 room_name도 추가해 줘야 한다. # room_id를 받을 자리를 만들어준다.
#     try:
#         room = Room.objects.get(pk=room_pk)
#         return render(
#             request,
#             "room_detail.html",
#             {
#                 "room": room,
#             },
#         )
#     except Room.DoesNotExist:  # 만약 try 안의 코드가 에러가 발생하면 except 안의 코드를 실행한다.
#         return render(
#             request,
#             "room_detail.html",
#             {
#                 "not_found": True,
#             },
#         )  # HttpResponse(f"see room with id: {room_pk}")
