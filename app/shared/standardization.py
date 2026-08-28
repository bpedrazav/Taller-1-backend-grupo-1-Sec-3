from typing import Generic, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    path: str
    success: bool
    code: int
    message: str
    data: Optional[T] = None
    error: Optional[str] = None

    @classmethod
    def respuesta_success(
        cls,
        path: str,
        code: int = 200,
        message: str = "Operación exitosa",
        data: Optional[T] = None,
    ):
        return cls(
            path=path,
            success=True,
            code=code,
            message=message,
            data=data,
            error=None,
        )

    @classmethod
    def respuesta_error(
        cls,
        path: str,
        code: int = 400,
        message: str = "Error en la operación",
        error: Optional[str] = None,
    ):
        return cls(
            path=path,
            success=False,
            code=code,
            message=message,
            data=None,
            error=error,
        )
