# Taller-1-backend-grupo-1-Sec-3

Parte 1: Estandarización en respuestas en JSON:

Success Status:  

1. path: "api/students" (example)
2. success: True (example)
3. code: 200 (example)
4. message: "Students retrieved successfully" (example)
5. data: [{"id": 1, "name": "Juan"}] (example)
  

Error status:  

1. path: "api/pets" (example)
2. success: False (example)
3. code: 404 (example)
4. error: "PetNotFoundException: line 28 in controllers/pet_controller.py" (example)
5. message: "The requested pet does not exist" (example)