from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(
    ModelViewSet
):  # ViewSet은 HTML form도 만들어 준다. 데이터 모양을 맞춰서 넣어줄 필요가 없어진다.
    serializer_class = CategorySerializer  # viewset은 serializer가 뭔지 알아야 한다.
    queryset = Category.objects.all()  # viewset의 object가 무엇인지 알아야 한다.


"""
class Categories(APIView):
    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(
                CategorySerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)


class CategoryDetail(APIView):
    def get_object(
        self, pk
    ):  # convention(관습). API의 상세한 부분을 작업할 때, category 한 개, room 한 개 이렇게 무언가를 하나만 찾을 때, URL의 상세한 부분을 작업할 때, 항상 get_object 객체를 가져와 get, put, delete mathod에서 공유한다.
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound
        # return category

    def get(self, request, pk):
        serializer = CategorySerializer(self.get_object(pk))
        print(serializer)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = CategorySerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)
"""

##################################################

# class CategoryViewSet(ModelViewSet):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.filter(
#         kind=Category.CategoryKindChoices.ROOMS,
#     )


# class CategoryViewSet(ModelViewSet):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()


# class Categories(APIView):
#     def get(self, request):
#         all_categories = Category.objects.all()
#         serializer = CategorySerializer(all_categories, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             new_category = serializer.save()
#             return Response(
#                 CategorySerializer(new_category).data,
#             )
#         else:
#             return Response(serializer.errors)


# class CategoryDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise NotFound

#     def get(self, request, pk):
#         serializer = CategorySerializer(self.get_object(pk))
#         return Response(serializer.data)

#     def put(self, request, pk):
#         serializer = CategorySerializer(
#             self.get_object(pk),
#             data=request.data,
#             partial=True,
#         )
#         if serializer.is_valid():
#             updated_category = serializer.save()
#             return Response(CategorySerializer(updated_category).data)
#         else:
#             return Response(serializer.errors)

#     def delete(self, request, pk):
#         self.get_object(pk).delete()
#         return Response(HTTP_204_NO_CONTENT)


# from rest_framework.decorators import api_view
# from rest_framework.exceptions import NotFound
# from rest_framework.response import Response
# from rest_framework.status import HTTP_204_NO_CONTENT
# from rest_framework.views import APIView:
# from .models import Category
# from .serializers import CategorySerializer


"""
QuerySet to JSON
And JSON to QuerySet. 장고는 양방향 번역기다.

GET POST /categories
GET PUT DELETE /categories/1
"""

"""
{
"name": "Category from DRF",
"kind": "rooms"
}
"""


# @api_view(["GET", "POST"])
# def categories(
#     request,
# ):  # decorator로 decorated된 API view 함수가 DB에 있는 모든 카테고리르 가져와서 serializer에게 넘겨주고 있다.
#     # serializer는 장고 객체를 JSON으로 번역해준다.
#     if request.method == "GET":
#         all_categories = Category.objects.all()
#         serializer = CategorySerializer(
#             all_categories,  # CategorySerializer에게 모든 카테고리를 준다.
#             many=True,  # 하나가 아닌 많은 카테고리를 보낸다고 알려주는 것이다.
#         )
#         return Response(serializer.data)
#     elif request.method == "POST":
#         print(
#             request.data
#         )  # {'name': 'Category from DRF', 'kind': 'rooms'} 가 출력된다. # user가 보내고 있는 데이터가 data에 들어있다.
#         serializer = CategorySerializer(
#             data=request.data
#         )  # Django에서 JSON으로 번역하고 싶을 때는 CategorySerializer에 category를 넘기고
#         # 만약 user로부터 데이터를 가져오고 싶다면 data를 CategorySerializer에게 넘겨준다.
#         """CategorySerializer는 우리가 views에서 serializer에게 어떻게 생겼는지를 설명해줬기에 데이터 형태를 모두 알고 있다."""
#         if serializer.is_valid():
#             new_category = (
#                 serializer.save()
#             )  # serializer.save를 하는 것 만으로도 serializer는 serializer 안에 있던 검증된 데이터로 create 메서드를 호출한다.
#             return Response(
#                 CategorySerializer(new_category).data,
#             )  # ({"created": True})
#         else:
#             return Response(serializer.errors)  # 계속해서 console을 열고 닫아주지 않아도 된다.
# print(serializer.is_valid())
# print(
#     serializer.errors
# )  # {'name': [ErrorDetail(string='This field is required.', code='required')]} 에러를 볼 수 있다.
# read_only=True를 pk와 created_at에 넣어주면 에러가 사라진다.
# return Response({"created": True})

# Category.objects.create( # 이렇게 해주면 유저가 보내는 데이터를 검증하지 않는 것이다.
#     name = request.data("name"),
#     kind = request.data("kind")
# )

#     {
#         "ok": True,
#         "categories": serializer.data,  # Category.objects.all(),
#     }
# )


# @api_view(["GET", "PUT", "DELETE"])
# def category(request, pk):  # url로부터 호출된 모든 view들은 request 객체를 받는다.
#     try:
#         category = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         raise NotFound

#     if request.method == "GET":
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = CategorySerializer(
#             category,
#             data=request.data,
#             partial=True,
#         )
#         if serializer.is_valid():
#             updated_category = serializer.save()
#             return Response(CategorySerializer(updated_category).data)
#         else:
#             return Response(serializer.errors)
#         # serializer = CategorySerializer(category)
#         # return Response(serializer.data)

#     elif request.method == "DELETE":
#         category.delete()
#         return Response(status=HTTP_204_NO_CONTENT)


# from django.http import JsonResponse
# from .models import Category

# # QuerySet to JSON


# def categories(request):
#     all_categories = Category.objects.all()
#     return JsonResponse({"ok": True})
