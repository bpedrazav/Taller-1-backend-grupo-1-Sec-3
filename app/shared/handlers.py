from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.shared.exceptions import APIException

def register_exception_handlers(app: FastAPI):
    
    @app.exception_handler(APIException)
    async def api_exception_handler(request: Request, exc: APIException):
        
        path_str = str(request.url.path).lstrip("/")
        
        return JSONResponse(
            status_code=exc.code,
            content={
                "path": path_str,
                "success": False,
                "code": exc.code,
                "error": exc.error,
                "message": exc.message
            }
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        path_str = str(request.url.path).lstrip("/")
        
        return JSONResponse(
            status_code=500,
            content={
                "path": path_str,
                "success": False,
                "code": 500,
                "error": f"{exc.__class__.__name__}: {str(exc)}",
                "message": "Internal Server Error"
            }
        )