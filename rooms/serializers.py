from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomDetailSerializer(ModelSerializer):
    owner = (
        TinyUserSerializer()
    )  # depth = 1로 전부 보여주는 것이 아닌 TinyUserSerializer를 사용하여 필요한 것만 보여준다.
    amenities = (
        AmenitySerializer(  # amenities는 많은 amenity들이 있는 list이다. 그래서 many=True를 써준다.
            many=True
        )
    )  # class 정의가 밑에 있으면 not defined 오류가 난다. 그래서 위로 올려준다.
    category = CategorySerializer()  # category는 하나의 category이다. 그래서 many=True를 쓰지 않는다.

    class Meta:
        model = Room
        fields = "__all__"
        # depth = 1


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (  # "__all__"
            "pk",
            "name",
            "country",
            "city",
            "price",
        )
        depth = 1  # room에 있는 모든 field를 보여준다. 하지만 보통 모든 데이터가 필요하지 않다.
