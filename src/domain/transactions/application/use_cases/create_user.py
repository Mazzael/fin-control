from pydantic import BaseModel
from src.core.either import Either
from src.core.either import left, right
from src.domain.transactions.enterprise.entities.user import User
from src.domain.transactions.application.repositories.users_repository import UsersRepository
from src.domain.transactions.application.cryptography.hash_generator import HashGenerator
from src.domain.transactions.application.use_cases.errors.user_already_exists_error import UserAlreadyExistsError

class CreateUserUseCaseRequest(BaseModel):
    name: str
    cpf: str
    password: str

class CreateUserUseCase:
    def __init__(self, users_repository: UsersRepository, hash_generator: HashGenerator):
        self.users_repository = users_repository
        self.hash_generator = hash_generator

    async def execute(self, request: CreateUserUseCaseRequest) -> Either[UserAlreadyExistsError, User]:
        user_with_same_cpf = await self.users_repository.find_by_cpf(request.cpf)

        if user_with_same_cpf:
            return left(UserAlreadyExistsError(identifier=request.cpf))

        hashed_password = await self.hash_generator.hash(request.password)

        user = User(name=request.name, cpf=request.cpf, password_hash=hashed_password, current_funds_in_cents=0)

        await self.users_repository.create(user)

        return right(user)
