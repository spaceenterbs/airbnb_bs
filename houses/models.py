from django.db import models


class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(
        max_length=140,
    )
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price",
        help_text="Positive Numbers Only",
    )
    description = models.TextField()
    address = models.CharField(
        max_length=140,
    )
    pets_allowed = models.BooleanField(
        verbose_name="Pets Allowed?",
        default=False,
        help_text="Does this house allow pets?",
    )

    house = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # SET_NULL로 하면 user가 삭제되어도 house는 남아있게 된다. 이는 쇼핑몰에서 사용자가 탈퇴해도 주문내역은 남아있는 것과 같다.
        # relationship을 변경했으니 migration을 해줘야 한다.
        related_name="houses",  # user.houses.all()을 통해 user가 만든 house들을 볼 수 있다.
    )  # Django한테 방의 가격처럼 단순한 숫자가 아닌 데이터를 houses 테이블에 저장한다고 알려준다. # 다른 앱에 있는 테이블의 object의 ID라는 걸 알려준다.

    def __str__(self):
        return self.name

    # 장고에서는 id가 pk이고, pk는 자동으로 만들어진다. (pk는 primary key의 약자)
