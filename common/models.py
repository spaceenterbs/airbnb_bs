from django.db import models


class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = (
            True  # abstract model은 DB에 나타나지 않는다. # abstract model은 admin에 나타나지 않는다.
        )
