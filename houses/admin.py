from django.contrib import admin
from .models import House


# Register your models here.
@admin.register(House)  # admin name; Houses 장고가 붙여줌 '-s'
class HouseAdmin(admin.ModelAdmin):
    list_filter = ["price_per_night", "pets_allowed"]
    search_fields = [
        "address__startswith"
    ]  # 정확히 그 검색어 아니게 정함. contains, endswith, 대문자 소문자 등등
    # exclude = ("price_per_night",)
