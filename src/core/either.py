from typing import Generic, TypeVar, Union

L = TypeVar('L')
R = TypeVar('R')

class Left(Generic[L, R]):
    def __init__(self, value: L):
        self.value = value

    def is_right(self) -> bool:
        return False

    def is_left(self) -> bool:
        return True

class Right(Generic[L, R]):
    def __init__(self, value: R):
        self.value = value

    def is_right(self) -> bool:
        return True

    def is_left(self) -> bool:
        return False

Either = Union[Left[L, R], Right[L, R]]

def left(value: L) -> Either[L, R]:
    return Left(value)

def right(value: R) -> Either[L, R]:
    return Right(value)
