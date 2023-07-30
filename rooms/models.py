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
        related_name="rooms",
    )
    amenities = models.ManyToManyField(  # room은 여러개의 amenity를 가질 수 있고, amenity는 여러개의 room을 가질 수 있다.
        "rooms.Amenity",
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",
    )

    def __str__(room) -> str:
        return room.name

    def total_amenities(
        room,
    ):  # admin이나 여기서 선언해주면 total_amenities라는 컬럼이 생기는데, 이 컬럼은 DB에 저장되지 않는다.(?)
        # print(self.amenities.all())  # 결과를 집접 보고 싶으면, 이렇게 출력하면 된다. 터미널에서 뜬다.
        return room.amenities.count()

    """관리자 페이지뿐만이 아닌 어딘가에서도 사용하고자 한다면, 모델 내부에. 그렇지 않다면 admin.py에."""
    # return room.amenities.all().count()
    # 대신 return self.amenities.filter().exclude().count() 해도 되긴 한다. 되긴...

    def rating(room):
        count = room.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            total_rating = 0
            print(
                room.reviews.all().values("rating")
            )  # <QuerySet [{'rating': 5}, {'rating': 3}, {'rating': 5}]> 아래의 최적화 버전.
            print(
                room.reviews.all()
            )  # <QuerySet [<Review: user / 5⭐>, <Review: user / 3⭐>, <Review: admin / 5⭐>]>
            for review in room.reviews.all().values("rating"):
                """values를 사용하면 QuerySet은 약간씩 바뀌어 더이상 review가 아니라 dict가 된다. 그래서 review.rating이 아니라 review["rating"]이 된다."""
                # for review in room.reviews.all(): # 숫자가 많아지면 부담이 커지는데, 장고가 전체 리뷰를 가져오게 하는 대신에, 우리가 할 수 있는 것은 원하는 값만 구체적으로 선택하는 것이다. 그럼 장고는 모든 걸 가져오지 않아도 되고, 오직 우리가 원하는 값만 가져올 것이다.
                total_rating += review["rating"]  # review.rating
            return round(total_rating / count, 2)


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
