from django.contrib import admin
from .models import Room, Amenity


@admin.action(
    description="Set all prices to zero"
)  # 관리자 페이지를 구축할 때, 동시에 여러 값들을 리셋하거나 수정할 때 액션을 사용할 수 있다. excel에 export 하는 것도 가능하다.
def reset_prices(
    model_admin,
    request,
    rooms,
):  # 세번째로 Queryset은 내가 선택한 모든 객체의 리스트다. 선택된 모든 객체를 주기에 그 객체들로 작업을 할 수 있다.
    # 두번째는 request 객체로, 이 액션을 누가 호출했는지에 대한 정보를 갖고 있다. 슈퍼유저인지, 일반유저인지 등등. 따라서 슈퍼 유저가 아니면 이 액션을 호출할 수 없다.
    # 첫번째는 액션을 호출하는 클래스다. # admin 액션은 3개의 매개변수로 호출된다.
    for room in rooms.all():
        room.price = 0
        room.save()  # 이제 내가 선택하는 방들은 새로운 price로 0을 가지게 된다.
        """ 그냥 함수를 만들고 admin.action decorator에 설명을 넣어 주고 admin 클래스 안의 actions에 그 함수를 추가하기만 하면 된다."""
    # print(model_admin)
    # print(dir(request))
    # print(rooms)
    # pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)
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
        "name",
        "^price",
        "-owner__username",  # ^는 username으로 시작하는 내용 찾음 # owner의 username으로 검색한다.
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
