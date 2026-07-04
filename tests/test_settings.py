from django.conf import settings


def test_custom_user_model_is_enabled() -> None:
    assert settings.AUTH_USER_MODEL == "users.User"

