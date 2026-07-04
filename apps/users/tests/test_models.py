import pytest

from apps.users.models import User


@pytest.mark.django_db
def test_create_user_uses_email_login() -> None:
    user = User.objects.create_user(email="player@example.com", password="secret123")

    assert user.email == "player@example.com"
    assert user.check_password("secret123")


@pytest.mark.django_db
def test_create_superuser_sets_admin_flags() -> None:
    user = User.objects.create_superuser(
        email="admin@example.com",
        password="secret123",
    )

    assert user.is_staff is True
    assert user.is_superuser is True

