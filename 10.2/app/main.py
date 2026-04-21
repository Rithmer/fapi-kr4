from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.schemas import UserPayload

app = FastAPI(title="Task 10.2")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation failed",
            "code": 422,
            "details": exc.errors(),
        },
    )


@app.post("/validate-user")
async def validate_user(payload: UserPayload) -> dict:
    return {"message": "Payload accepted", "user": payload.model_dump()}
