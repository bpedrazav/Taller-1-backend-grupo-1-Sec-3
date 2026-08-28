from fastapi import APIRouter, Request

from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service
from app.shared.standardization import ApiResponse 

router = APIRouter(
    prefix="/api/students/{student_id}/pets",
    tags=["Pets"],
)


@router.get("", response_model=ApiResponse[list[Pet]])
def find_all(request: Request, student_id: str) -> ApiResponse[list[Pet]]:
    data = pets_service.find_all_for_student(student_id)
    return ApiResponse.respuesta_success(
        path=request.url.path, data=data
    )

@router.post("", status_code=201, response_model=ApiResponse[Pet])
def create(request: Request, student_id: str, body: CreatePetDto) -> ApiResponse[Pet]:
    data = pets_service.create(student_id, body)
    return ApiResponse.respuesta_success(
        path=request.url.path, code=201, message="pet created" , data=data
    )


@router.patch("/{pet_id}", response_model=ApiResponse[Pet])
def update(request: Request, student_id: str, pet_id: str, body: UpdatePetDto) -> ApiResponse[Pet]:
    data = pets_service.update(student_id, pet_id, body)
    return ApiResponse.respuesta_success(
        path=request.url.path, message="pet updated", data=data
)


@router.delete("/{pet_id}", response_model=ApiResponse[Pet])
def delete(request: Request, student_id: str, pet_id: str) -> ApiResponse[Pet]:
    data = pets_service.delete(student_id, pet_id)
    return ApiResponse.respuesta_success(
        path=request.url.path, message="pet deleted", data=data
    )