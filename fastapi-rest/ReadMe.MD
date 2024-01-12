### Python REST API based on FastAPI framework, TDD, BDD development

### Commands to execute

- Install Postgresql
- install Python 3.9 + version
- Create virtual environment
  - python3 -m venv venv
- Install required libraries
  - pip install requirements.txt
- Run server
  - uvicorn app.main:app --reload
- Unit testing
  - pytest --html=reports.html tests/
- BDD tests
  - pytest-bdd features/


### Tech Stack

| Technology   | Usage                |
|--------------|----------------------|
| Python 3     | Runtime              |
| FastAPI      | REST Framework       |
| Pydantic     | Schema Generator     |
 | SQLAlchemy   | ORM                  |
| psycopg2     | postgresql driver    | 

