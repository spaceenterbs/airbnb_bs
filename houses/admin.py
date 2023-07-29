from django.contrib import admin
from .models import House  # model의 클래스인 House를 import


@admin.register(House)  # admin.site.register(House, HouseAdmin)과 같은 의미
class HouseAdmin(admin.ModelAdmin):  # admin.ModelAdmin을 상속받는 HouseAdmin 클래스 생성
    # fields = (
    #     "name",
    #     "address",
    #     ("price_per_night", "pets_allowed"),
    # )
    list_display = (
        "name",
        "price_per_night",
        "address",
        "pets_allowed",
    )
    list_filter = (
        "pets_allowed",
        "price_per_night",
    )

    # search_fields = ("address__startswith",)  # ends, contains, icontains, iexact, exact
    # # tuple에 쉼표 안 붙여주면 오류 난다. 괄호 없애서.

    # # exclude = ("price_per_night",)

    # list_display_links = (
    #     "name",
    #     "address",
    # )
    # list_editable = ("pets_allowed",)
