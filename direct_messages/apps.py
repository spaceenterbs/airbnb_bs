from django.apps import AppConfig


class DirectMessagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "direct_messages"
    verbose_name = (
        "Direct Messages"  # 장고는 대부분의 경우 올바른 이름을 찾아서 적어주지만, 이름에 밑줄이 들어 가는 건 어떻게 해주지 못한다.
    )
