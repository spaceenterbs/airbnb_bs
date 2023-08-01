from rest_framework import serializers
from .models import Category

# serializer은 번역기일 뿐이다. Django 코드를 API가 필요로 하는 JSON 코드로 바꿔주는 것이다.
# 예를 들어, 카테고리를 포함해 DB에 있는 객체들은 PK가 있다. 그래서 아래와 같이 pk를 넣어주면, serializer는 이를 JSON으로 바꿔준다.
# 1. 어떻게 번역할지, 2. 무엇을 번역할지. 우리는 무엇을 보여주고 무엇을 안 보여줄지 고를 수 있다.


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"  # category model의 모든 field를 보여주겠다. created와 updated는 숨겨져있다.
        # fields = ( # this or
        #     "name",
        #     "kind",
        # )
        # exclude = ( # this
        #     "name",
        #     "kind",
        # )

    # class CategorySerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Category
    #         fields = (
    #             "pk",
    #             "name",
    #             "kind",
    #         )

    # class CategorySerializer(
    #     serializers.Serializer
    # ):  # name과 kind가 있는 카테고리를 번역하기 위해 만들어 졌는데, CategorySerializer(all_categories)를 하면 serializer에게 카테고리 하나만 넘긴 것이 아닌, 모든 카테고리를 넘긴 것이 된다. 하나 vs 리스트.
    #     # 카테고리가 어떻게 JSON으로 변환될 지 커스텀할 수 있도록 해준다. # models.Model과 비슷하다.
    #     pk = serializers.IntegerField(read_only=True)  # or CharField, whatever is possible.
    #     name = serializers.CharField(
    #         required=True,
    #         max_length=50,  # serializer에게 우리 데이터의 형태를 설명하고 있다.
    #     )
    #     kind = serializers.ChoiceField(
    #         # max_length=15,
    #         choices=Category.CategoryKindChoices.choices,
    #     )
    #     created_at = serializers.DateTimeField(
    #         read_only=True
    #     )  # 이렇게 해주면 값이 또 들어간다. 그러나, 반복되는 코드가 많아서 노마드에서 이를 나중에 해결해준다.

    #     def create(self, validated_data):
    #         # print(validated_data)
    #         return Category.objects.create(
    #             **validated_data
    #         )  # 이를 통해 공식적으로 DB에 카테고리를 만들 수 있다. serializer의 description에 따라 검증도 된 것을 알 수 있다.

    #     def update(self, instance, validated_data):
    #         instance.name = validated_data.get("name", instance.name)
    #         instance.kind = validated_data.get("kind", instance.kind)
    #         instance.save()
    #         return instance

    """
        {'name': 'Category from DRF', 'kind': 'rooms'}

        name = 'Category from DRF',
        kind = 'rooms'
        위의 딕셔너리를 아래와 같이 바꿔준다.

        create는 객체를 반환해야 한다.
        """


# class Meta:
#     model = Category
#     fields = "__all__"
