from fastapi import APIRouter

from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service
from app.shared.standardization import ApiResponse 

router = APIRouter(
    prefix="/api/students/{studentId}/pets",
    tags=["Pets"],
)


@router.get("")
def find_all(studentId: str) -> list[Pet]:
    data = pets_service.find_all_for_student(studentId)
    return ApiResponse.respuesta_success(
        path=f"/api/students/{studentId}/pets", data=data
    )

@router.post("", status_code=201)
def create(studentId: str, body: CreatePetDto) -> Pet:
    data = pets_service.create(studentId, body)
    return ApiResponse.respuesta_success(
        path=f"/api/students/{studentId}/pets", code=201, data=data
    )


@router.patch("/{petId}")
def update(studentId: str, petId: str, body: UpdatePetDto) -> Pet:
    data = pets_service.update(studentId, petId, body)
    return ApiResponse.respuesta_succes(
        path=f"/api/students/{studentId}/pets", data=data
    )


@router.delete("/{petId}")
def delete(studentId: str, petId: str) -> Pet:
    data = pets_service.delete(studentId, petId)
    return ApiResponse.respuesta_succes(
        path=f"/api/students/{studentId}/pets", data=data
    )