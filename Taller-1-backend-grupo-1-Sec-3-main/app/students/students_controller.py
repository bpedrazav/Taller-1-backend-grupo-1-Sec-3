from fastapi import APIRouter, Request
from app.shared.standardization import ApiResponse
from app.pets.pets_service import pets_service
from app.students.students_schemas import CreateStudentDto, Student, UpdateStudentDto
from app.students.students_service import students_service

router = APIRouter(prefix="/api/students", tags=["Students"])


@router.get("", response_model=ApiResponse[list[Student]])
def find_all(request: Request):
    data = students_service.find_all()
    return ApiResponse.respuesta_success(
        path=request.url.path,
        code=200,
        message="se han obtenido exitosamente los estudiantes",
        data = data
    )

@router.get("/{student_id}, response_model=ApiResponse[Student]")
def find_by_id(request: Request, student_id: str):
    data = students_service.find_by_id(student_id)
    return ApiResponse.respuesta_success(
        path=request.url.path,
        code=200,
        message="estudiante obtenido con exito",
        data = data
    )


@router.post("", status_code=201, response_model=ApiResponse[Student])
def create(request: Request, body: CreateStudentDto):
    data = students_service.create(body)
    return ApiResponse.respuesta_success(
        path=request.url.path,
        code=201,
        message="estudiante creado exitosamente",
        data = data
    )


@router.patch("/{student_id}", response_model=ApiResponse[Student])
def update(request: Request, student_id: str, body: UpdateStudentDto):
    data = students_service.update(student_id, body)
    return ApiResponse.respuesta_success(
        path=request.url.path,
        code=200,
        message="estudiante correctamente actualizado",
        data = data
    )

@router.delete("/{student_id}", response_model=ApiResponse[Student])
def delete(request: Request, student_id: str):
    deleted = students_service.delete(student_id)
    pets_service.delete_all_for_student(student_id)
    return ApiResponse.respuesta_success(
        path=request.url.path,
        code=200,
        message="estudiante eliminado correctamente",
        data = deleted
    )