from fastapi.testclient import TestClient
from fastapi import status
from app.main import app
from app.schemas import ProductBase

client = TestClient(app=app)


def test_get_products():
    response = client.get("/products")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() is not None


def test_create_product():
    product = ProductBase(name="Baby Jumper", cost=30)
    print(product.model_dump())
    response = client.post("/products", json=product.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() is not None
