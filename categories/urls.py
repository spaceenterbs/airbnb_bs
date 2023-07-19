from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.CategoryViewSet.as_view(
            {
                "get": "list",  # http 메서드를 class 메서드와 이어준다.
                "post": "create",
            }
        ),
    ),  # ViewSet의 메소드와 사용자가 나한테 보낼 HTTP 메소드를 연결해주면 땡.
    # Categories
    path(
        "<int:pk>",  # URL에서 pk를 받을 수 있도록 해줘야 한다. ViewSet은 pk가 필수임.
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),  # CategoryDetail
]
