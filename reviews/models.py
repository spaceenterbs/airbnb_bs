from django.db import models
from common.models import CommonModel


class Review(CommonModel):

    """Review from a User to a Room or Experience"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviews",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    payload = models.TextField()  # 유저들이 남기는 리뷰 = 텍스트
    rating = models.PositiveIntegerField()  # 유저들이 남기는 리뷰 = 별점

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}⭐"
