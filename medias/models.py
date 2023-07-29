from django.db import models
from common.models import CommonModel


class Photo(CommonModel):

    """Photo Model Definition"""

    file = models.ImageField()
    description = (  # Video와 다르게 설명이 필요하다.
        models.CharField(  # Textfield가 아닌 제한을 둔 Charfield를 사용한다.
            max_length=140,
        )
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):

    """Video Model Definition"""

    file = models.FileField()  # VideoField는 없다.
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Video File"
