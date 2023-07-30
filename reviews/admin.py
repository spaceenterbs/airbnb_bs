from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by word!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),  # url에 모두 표시된다. 장고는 url을 읽고, 나에게 필터링한 결과를 준다.
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        # print(self.value()) 같이 하면 실제로 url을 읽어서 그걸 뽑아내지 않아도 된다. # print(request.get)의 출력값인 {'word': ['good']}을 가져와서 배열에서 단어를 빼내온다.
        # print(dif(request)) # 단어로 필터링을 해보자.
        # print(reviews) # 이 review들을 필터링한 다음 리턴해야 한다.
        if word:
            return reviews.filter(
                payload__contatins=word
            )  # models.py의 payload에 word가 포함되어 있는지 확인한다.
        else:
            reviews


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
