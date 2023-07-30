from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",  # 모델의 속성들 뿐만 아니라 메소드도 사용할 수 있다.
        "owner",
        "created_at",
    )

    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "owner__username",  # owner의 username으로 검색한다.
        # "^name",  # name으로 시작하는 것을 검색한다.
        # "=price",  # price로 시작하는 것을 검색한다. ^를 빼주면 price가 포함된 것을 검색한다.
        # # = (exact)는 정확히 일치하는 것을 검색한다.
    )

    # def total_amenities(self, room):
    #     return room.amenities.count()


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (  # 내부에서도 보여진다.
        "created_at",
        "updated_at",
    )
