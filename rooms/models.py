from django.db import models
from common.models import CommonModel


class Room(CommonModel):

    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = "shared_room", "Shared Room"

    name = models.CharField(
        max_length=180,
        default="",  # 이미 만들어져있는 유저 때문에 name 필드를 추가하면 스트링을 넣어줘야 한다.
    )
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(  # room은 하나의 user를 가질 수 있고, user는 여러개의 room을 가질 수 있다.
        "users.User",
        on_delete=models.CASCADE,
    )
    amenities = models.ManyToManyField(  # room은 여러개의 amenity를 가질 수 있고, amenity는 여러개의 room을 가질 수 있다.
        "rooms.Amenity",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self) -> str:
        return self.name

    def total_amenities(
        self,
    ):  # admin이나 여기서 선언해주면 total_amenities라는 컬럼이 생기는데, 이 컬럼은 DB에 저장되지 않는다.(?)
        print(self.amenities.all())
        return self.amenities.all().count()


class Amenity(CommonModel):

    """Amenity Definition"""

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        null=True,  # null=True만 있으면 값을 입력해줘야 하기에 밑에 blank=True를 추가해준다.
        blank=True,  # admin에서 description을 입력하지 않아도 된다. 장고 form에서의 공백을 의미함.
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"  # admin에서 복수형으로 보이게 해준다.
