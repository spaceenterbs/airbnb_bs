from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by word!"

    parameter_name = "word"  # url에 표시되는 것은 parameter_name이다.

    def lookups(self, request, model_admin):  # 튜플의 리스트를 리턴해야 하는 함수가 lookups이다.
        # 튜플의 첫번째 요소는 url에 나타날 값이고, 두번째 요소는 유저가 보고 클릭하게 되는 텍스트다.
        return [
            ("good", "Good"),  # url에 모두 표시된다. 장고는 url을 읽고, 나에게 필터링한 결과를 준다.
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):  # 필터링된 객체인 review를 리턴해야 하는 메소드다.
        word = self.value()  # url에 있는 값을 가져오기 위해 self.value를 호출하기만 하면 된다.
        # print(self.value()) 같이 하면 실제로 url을 읽어서 그걸 뽑아내지 않아도 된다. # print(request.get)의 출력값인 {'word': ['good']}을 가져와서 배열에서 단어를 빼내온다.
        # print(dir(request)) # 단어로 필터링을 해보자.
        # print(reviews) # 이 review들을 필터링한 다음 리턴해야 한다.
        if word:
            return reviews.filter(
                payload__contatins=word  # word는 url에 있던 것이다.
            )  # models.py의 payload에 word가 포함되어 있는지 확인한다.
        else:
            reviews  # 만약 url에 어떠한 단어도 없다면, url에 word가 없고 그럴 때도 우린 여전히 모든 리뷰를 리턴해야 한다.
            # 이것이 '모든 리뷰를 리턴하는 것'이다.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        "rating",
        "user__is_host",  # relationship으로도 필터링을 할 수 있다. foreign key를 통해 필터링을 할 수 있다.
        "room__category",  # category가 또 다른 foreign key를 가지면 외래키의 외래키 filter도 가능하다. # room의 category 또한 foreign key이지만 필터링을 할 수 있다.
        "room__pet_friendly",
    )
