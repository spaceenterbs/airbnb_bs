from django.db import models
from common.models import CommonModel


class Experience(CommonModel):

    """Experience Model Definition"""

    country = models.CharField(  # country와 city가 중복되니 다른 모델에서 가져옴
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    name = models.CharField(
        max_length=250,
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=250,
    )
    start = models.TimeField()  # 시간, 분, 초
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField(  # 특전, what is included. experience는 여러개의 perk를 가질 수 있고, perk는 여러개의 experience를 가질 수 있다.
        "experiences.Perk",  # Perk 모델을 참조
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):

    """What is included on an Experiences"""

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        default="",  # null=True로 하면 빈칸이 들어가는데, 이건 빈칸이 아니라 빈 문자열이 들어가야 하기 때문에 default를 설정해준다. 둘을 같이 설정하면 빈칸이 들어가는 것을 허용한다는 뜻이 된다. 비슷하다.
    )
    explanation = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self) -> str:
        return self.name
