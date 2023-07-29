from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (  # 관리자 페이지에서 model의 field가 보이는 순서를 설정할 수 있게 해준다.  # tuple 안에 dictionary가 들어가는 구조
            "Profile",  # fieldset의 이름 = Profile
            {
                "fields": (
                    "avatar",  # fieldset 안에 들어가는 field들
                    "username",
                    "password",
                    "name",
                    "email",
                    "is_host",
                    "gender",
                    "language",
                    "currency",
                ),  # tuple
                "classes": ("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": (
                    "collapse",
                ),  # fieldset을 접을 수 있게 해준다. ("collapse" or "wide") wide는 더 넓어진다.
            },
        ),
        (
            "Important dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    )
    #         {
    #             "fields": (
    #                 "avatar",
    #                 "username",
    #                 "password",
    #                 "name",
    #                 "email",
    #                 "is_host",
    #                 "gender",
    #                 "language",
    #                 "currency",
    #             ),
    #             "classes": ("wide",),
    #         },
    #     ),
    #     (
    #         "Permissions",
    #         {
    #             "fields": (
    #                 "is_active",
    #                 "is_staff",
    #                 "is_superuser",
    #                 "groups",
    #                 "user_permissions",
    #             ),
    #         },
    #     ),
    #     (
    #         "Important dates",
    #         {
    #             "fields": ("last_login", "date_joined"),
    #         },
    #     ),
    # )

    # fieldsets = None
    # fields = ("email", "password", "name") # fielsets와 다르게 fields는 이름도 붙일 수 있고 확장가능하게 만들 수도 있다.

    list_display = (
        "username",
        "email",
        "name",
        "is_host",
    )  # 원래 있던 firstname lastname을 안 보이게 하고 name을 보이게 한다.
    # fields = ("email", "password", "name")
