"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from rooms import views

# from rooms import views as room_views  # as는 별칭을 붙여준다.
# from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path(
    #     "rooms/", views.say_hello
    # ),  # views.say_hello argument는 유저가 이 url로 왔을 때 장고가 실행할 함수이다.
    path(
        "api/v1/rooms/", include("rooms.urls")
    ),  # 누군가 rooms/(뒤에 뭐가 붙든) 에 접근한다면 rooms.urls 파일을 찾아보라는 말이다.
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/experiences/", include("experiences.urls")),
]

"""
    /rooms
    /rooms/1
    /rooms/1/edit
    /rooms/1/delete
    /users
    /users/1
    /users/1/edit
    /users/login
    /users/create-account
    /reviews
    /reviews/1
    /reviews/1/edit
    등 수많은 url을 만들어야 한다.
    따라서 rooms url을 개별 파일로 분리하는 작업을 거친다.

    분할 정복을 실현하는 것인데,
    모든 앱은 각자에 대한 개별적인 urls 파일을 가지게 되고,
    그러고 나서 config의 urls.py 파일은 이 모든 파일들을 하나로 합치는 역할을 할 것이다.
    그리고 전체 구조는 분산된다.
"""
