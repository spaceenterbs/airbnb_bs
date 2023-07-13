from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    """Room and Experience Category"""

    name = models.CharField(
        max_length=50,
    )

    kind = models.CharField(
        max_length=3,
    )
