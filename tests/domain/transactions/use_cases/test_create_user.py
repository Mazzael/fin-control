from unittest.mock import MagicMock, AsyncMock
import pytest
from src.domain.transactions.application.use_cases.create_user import CreateUserUseCase, CreateUserUseCaseRequest
from src.domain.transactions.enterprise.entities.user import User
from src.domain.transactions.application.use_cases.errors.user_already_exists_error import UserAlreadyExistsError

@pytest.mark.asyncio
async def test_create_user_success():
    # Arrange
    users_repository_mock = MagicMock()
    users_repository_mock.find_by_cpf = AsyncMock(return_value=None)
    users_repository_mock.create = AsyncMock()

    hash_generator_mock = MagicMock()
    hash_generator_mock.hash = AsyncMock(return_value="hashed_password")

    use_case = CreateUserUseCase(users_repository_mock, hash_generator_mock)

    request = CreateUserUseCaseRequest(
        name="John Doe",
        cpf="12345678900",
        password="securepassword",
    )

    # Act
    result = await use_case.execute(request)

    print(result.value, 'result')

    # Assert
    assert result.is_right(), "Expected a successful result"
    assert isinstance(result.value, User), "Expected result to be a User instance"
    users_repository_mock.find_by_cpf.assert_awaited_once_with("12345678900")
    hash_generator_mock.hash.assert_awaited_once_with("securepassword")
    users_repository_mock.create.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_user_already_exists():
    # Arrange
    existing_user = User(name='Existing User', cpf='12345678900', password_hash='hashed_password', current_funds_in_cents=0)

    users_repository_mock = MagicMock()
    users_repository_mock.find_by_cpf = AsyncMock(return_value=existing_user)

    hash_generator_mock = MagicMock()

    use_case = CreateUserUseCase(users_repository_mock, hash_generator_mock)

    request = CreateUserUseCaseRequest(
        name="John Doe",
        cpf="12345678900",
        password="securepassword",
    )

    # Act
    result = await use_case.execute(request)

    # Assert
    assert result.is_left(), "Expected an error result"
    assert isinstance(result.value, UserAlreadyExistsError), "Expected result to be UserAlreadyExistsError"
    users_repository_mock.find_by_cpf.assert_awaited_once_with("12345678900")
    hash_generator_mock.hash.assert_not_called()
