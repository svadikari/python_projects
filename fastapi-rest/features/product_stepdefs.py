from pytest_bdd import scenario, given, when, then, parsers
import requests
from app.schemas import ProductBase

PRODUCT_URL = 'http://localhost:8000/products'


@scenario("product.feature", "Create Product Item")
def test_product_create():
    print('Create Product Item Completed!!')
    pass


@given("Item payload is prepared", target_fixture="product_request")
def prepare_product():
    print("Item payload prepared!!!")
    input_data = {"name": "Baby Pant", "cost": 12.5}
    product = ProductBase(**input_data)
    product.cost = 12.5
    return product


@when("Item create call initiated", target_fixture="response")
def initiate_product_create(product_request):
    print(" ITEM CREATED!!")
    return requests.post(PRODUCT_URL, json=dict(product_request))


@then(parsers.parse('Item is persisted and service returns with {expected_status: d} status'))
def validate_response(expected_status, product_request, response):
    assert expected_status == response.status_code
    assert product_request.name == response.json()["name"]
    assert product_request.cost == response.json()["cost"]


@scenario("product.feature", "Fetch Product Detail")
def test_product_fetch():
    print('Fetch Product Item Completed!!')


@given(parsers.parse('There are give products exists for {product_id:d}'), target_fixture="product_id")
def product_identifier(product_id):
    return product_id


@when(parsers.parse("Product fetch call initiated for {product_id:d}"), target_fixture="response")
def initiate_product_fetch(product_id):
    return requests.get(f'{PRODUCT_URL}/{product_id}')


@then(parsers.parse("Product service responds with {expected_status:d} status"))
def validate_fetch_response(expected_status, response):
    assert expected_status == response.status_code
