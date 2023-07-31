from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


@api_view()
def categories(request):
    all_categories = Category.objects.all()
    serializer = CategorySerializer(
        all_categories,  # CategorySerializer에게 모든 카테고리를 준다.
        many=True,  # 하나가 아닌 많은 카테고리를 보낸다고 알려주는 것이다.
    )
    return Response(
        {
            "ok": True,
            "categories": serializer.data,  # Category.objects.all(),
        }
    )


# from django.http import JsonResponse
# from .models import Category

# # QuerySet to JSON


# def categories(request):
#     all_categories = Category.objects.all()
#     return JsonResponse({"ok": True})


# from rest_framework.decorators import api_view
# from rest_framework.exceptions import NotFound
# from rest_framework.response import Response
# from rest_framework.status import HTTP_204_NO_CONTENT
# from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet
# from .models import Category
# from .serializers import CategorySerializer


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
