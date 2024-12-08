from src.core.errors.use_case_error import UseCaseError

class UserAlreadyExistsError(UseCaseError):
    def __init__(self, identifier: str):
        super().__init__(f'User "{identifier}" already exists.')
        self._message = f'User "{identifier}" already exists.'

    @property
    def message(self) -> str:
        return self._message
