from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")  # value, label for the admin panel
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")  # has to be shorter than maximum length
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"  # tuple이 아니어도 됨
        USD = "usd", "US DOllar"

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )  # editable 속성을 달면 관리자 패널에 안 나옴

    avatar = models.ImageField(blank=True)  # blank=True: 필수가 아님
    profile_photo = models.ImageField()
    name = models.CharField(
        max_length=150,
        default="",  # 이미 만들어져있는 유저 때문에 name 필드를 추가하면 스트링을 넣어줘야 한다. # charfield
    )  # models.py 수정할 때마다 makemigrations, migrate 해줘야 함; db와 같지 않으니까

    is_host = models.BooleanField(  # 집을 빌려주는 호스트인가? 여행자인가?
        default=False
    )  # default=False or null=True, 이미 만들어져있는 유저 때문에 is_host 필드를 추가하면 NULL이 되기 때문에 # boolean # 이전 사용자에게도 값을 주고 이후 사용자에게도 값을 주기 위해 default 값을 준다.
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


# User (Django)

# profile 모델을 만들어서 user와 연결한다. (>User) # user는 그대로 두고 prifile 모델에 프로필 이미지, 카카오톡 로그인, 페이스북 로그인 같은 것들을 넣는다.
