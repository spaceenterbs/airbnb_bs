from django.db import models
from common.models import CommonModel


class Booking(CommonModel):

    """Booking Model Definition"""

    class BookingKindChoices(models.TextChoices):  # 이게 어떤 예약을 나타내는지 알려줄 것이다.
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,  # experience 예약만도 할 수 있게 하기 위해
        blank=True,  # 어드민 패널에서 이 부분을 채울 필요가 없다.
        on_delete=models.SET_NULL,  # 유저가 만든 예약의 내역들을 기록하고 싶을 수도 있으므로
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    check_in = (
        models.DateField(  # null=True, blank=True를 해주면 사용되든 사용되지 않든 상관없이 DB에 저장이 된다.
            null=True,
            blank=True,
        )
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )
    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    guests = models.PositiveIntegerField()

    def __str__(self):
        return (
            f"{self.kind.title()} / Booking for: {self.user}"  # kind와 user를 보여주는 것이다.
        )
