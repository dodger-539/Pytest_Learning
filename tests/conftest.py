import pytest

# Для примера создадим простой класс пользователя
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def is_admin(self):
        return self.role == "admin"

@pytest.fixture
def admin_user():
    """Фикстура, создающая объект пользователя с правами админа."""
    print("\n[conftest] Создание admin_user")
    return User(name="Admin", role="admin")