from collections.abc import Callable
from typing import ParamSpec, TypeVar

_P = ParamSpec('_P')
_T = TypeVar('_T')


class RateLimitDecorator:
    def __init__(self,
                 calls: int = ...,
                 period: float = ...,
                 clock: float = ...,
                 raise_on_limit: bool = ...) -> None:
        ...

    def __call__(self, func: Callable[_P, _T]) -> Callable[_P, _T]:
        ...


def sleep_and_retry(func: Callable[_P, _T]) -> Callable[_P, _T]:
    ...
