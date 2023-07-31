from rest_framework import serializers

# from .models import Category

# serializer은 번역기일 뿐이다. Django 코드를 API가 필요로 하는 JSON 코드로 바꿔주는 것이다.
# 예를 들어, 카테고리를 포함해 DB에 있는 객체들은 PK가 있다. 그래서 아래와 같이 pk를 넣어주면, serializer는 이를 JSON으로 바꿔준다.
# 1. 어떻게 번역할지, 2. 무엇을 번역할지. 우리는 무엇을 보여주고 무엇을 안 보여줄지 고를 수 있다.


class CategorySerializer(
    serializers.Serializer
):  # name과 kind가 있는 카테고리를 번역하기 위해 만들어 졌는데, CategorySerializer(all_categories)를 하면 serializer에게 카테고리 하나만 넘긴 것이 아닌, 모든 카테고리를 넘긴 것이 된다. 하나 vs 리스트.
    # 카테고리가 어떻게 JSON으로 변환될 지 커스텀할 수 있도록 해준다. # models.Model과 비슷하다.
    pk = serializers.IntegerField(read_only=True)  # or CharField, whatever is possible.
    name = serializers.CharField(
        required=True,
        max_length=50,  # serializer에게 우리 데이터의 형태를 설명하고 있다.
    )
    kind = serializers.CharField(
        max_length=15,
    )
    created_at = serializers.DateTimeField(
        read_only=True
    )  # 이렇게 해주면 값이 또 들어간다. 그러나, 반복되는 코드가 많아서 노마드에서 이를 나중에 해결해준다.

    # class Meta:
    #     model = Category
    #     fields = "__all__"
