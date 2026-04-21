from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions import CustomExceptionA, CustomExceptionB
from app.schemas import ErrorResponse

app = FastAPI(title="Task 10.1")


@app.exception_handler(CustomExceptionA)
async def custom_exception_a_handler(_: Request, exc: CustomExceptionA) -> JSONResponse:
    payload = ErrorResponse(error=exc.message, code=418)
    return JSONResponse(status_code=418, content=payload.model_dump())


@app.exception_handler(CustomExceptionB)
async def custom_exception_b_handler(_: Request, exc: CustomExceptionB) -> JSONResponse:
    payload = ErrorResponse(error=exc.message, code=404)
    return JSONResponse(status_code=404, content=payload.model_dump())


@app.get("/exception-a", response_model=ErrorResponse, responses={418: {"model": ErrorResponse}})
async def raise_custom_a(should_fail: bool = True) -> ErrorResponse:
    if should_fail:
        raise CustomExceptionA("CustomExceptionA was triggered")
    return ErrorResponse(error="No error", code=200)


@app.get("/exception-b/{resource_id}", response_model=ErrorResponse, responses={404: {"model": ErrorResponse}})
async def raise_custom_b(resource_id: int) -> ErrorResponse:
    if resource_id != 1:
        raise CustomExceptionB("CustomExceptionB: resource not found")
    return ErrorResponse(error="Resource exists", code=200)
