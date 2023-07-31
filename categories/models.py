# catergories를 별도의 app에 두는 이유는 categories가 두 개의 다른 app에서 사용될 수 있기 때문이다.
# room과 experience가 categories를 공유할 수 있다.
# 그렇다고 다른 모든 모델들을 애플리케이션으로 만들 필요는 없다; direct_messages의 chatting rooms와 messages가 같은 앱에 있는 것과 같이.
from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    """Room or Experience Category"""

    class CategoryKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(
        max_length=50,
    )

    kind = models.CharField(
        max_length=15,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind.title() }: {self.name}"  # title()은 첫글자만 대문자로 바꿔준다.

    class Meta:
        verbose_name_plural = "Categories"


# from django.db import models
# from common.models import CommonModel


# class Category(CommonModel):

#     """Room or Experience Category"""

#     class CategoryKindChoices(models.TextChoices):
#         ROOMS = "rooms", "Rooms"
#         EXPERIENCES = "experiences", "Experiences"

#     name = models.CharField(max_length=50)
#     kind = models.CharField(
#         max_length=15,
#         choices=CategoryKindChoices.choices,
#     )

#     def __str__(self) -> str:
#         return f"{self.kind.title()}: {self.name}"

#     class Meta:
#         verbose_name_plural = "Categories"
