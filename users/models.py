from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")  # value, label
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "US DOllar"

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150, editable=False
    )  # editable 속성을 달면 관리자 패널에 안 나옴

    avatar = models.ImageField(blank=True)  # blank=True: 필수가 아님
    name = models.CharField(
        max_length=150,
        default="",  # 이미 만들어져있는 유저 때문에 name 필드를 추가하면 스트링을 넣어줘야 한다.
    )  # models.py 수정할 때마다 makemigrations, migrate 해줘야 함; db와 같지 않으니까

    is_host = models.BooleanField(
        default=False
    )  # default=False or null=True, 이미 만들어져있는 유저 때문에 is_host 필드를 추가하면 NULL이 되기 때문에
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,  # choices가 textchoices를 상속받았기 때문에 choices.choices로 사용 가능
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
    )
