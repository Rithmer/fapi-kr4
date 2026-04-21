from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Product

app = FastAPI(title="Task 9.1")


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products")
def list_products(db: Session = Depends(get_db)) -> list[dict]:
    rows = db.query(Product).all()
    return [
        {
            "id": row.id,
            "title": row.title,
            "price": row.price,
            "count": row.count,
            "description": row.description,
        }
        for row in rows
    ]
