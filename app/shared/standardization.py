from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')

class ApiResponse(BaseModel, Generic[T]):
    path: str
    success: bool
    code: int
    message: str
    data: Optional[T] = None
    error: Optional[str] = None