Orders
--------------------------

## Installation steps
pip3 install fastapi  -- rest framework<br/>
pip3 install "uvicorn[standard]" -- web application <br/>
pip3 install email_validator -- email validator <br/>
pip3 install passlib -- password decrypt <br/>
pip3 install bcrypt -- password decryption algorithm <br/> 
pip3 install psycopg2 -- Postgres driver package <br/>
pip3 install sqlalchemy -- ORM package <br/>
pip3 install "python-jose[cryptography]" -- JWT Token <br/>

pip3 install -r requirements.txt (installs all libraries from requirements.txt file)



## Run Application Server

uvicorn api.main:app --reload

## Database migration tool
https://alembic.sqlalchemy.org/en/latest/tutorial.html <br/>
pip3 install alembic <br/>
alembic init <directory> (ex: alembic init db_migrations) <br/>
remove value from sqlalchemy.url = in alembic.ini file <br/>
add database configuration in env.py file as below  <br/>
config.set_main_option("sqlalchemy.url", f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_db}") <br/>
#### update target_metadata as below <br/>
target_metadata = [users.Base.metadata] <br/>
we care remove metadata configuration from application main.py file 
#### Autogenerate migration file and migrate changes
alembic revision --autogenerate -m "users, orders tables create" <br/>
alembic current <br/>
alembic upgrade <revision#> OR alembic upgrade head OR alembic upgrade +1<br/>
alembic downgrade <revision#> OR alembic downgrade -1 <br/>




## Deploy to Heroku 
Create an account in heroku.com

Login: heroku login <br/>
Clone the repo: heroku git:clone -a shyam-orders <br/>
cd shyam-orders <br/>
git add . <br/>
git commit -am "initial commit" <br/>
git push heroku master <br/>
heroku logs --tail <br/>
heroku ps:restart <app_name> (start application) <br/>
heroku ps:stop <app_name> (stop application) <br/>

### Data base migration using alembic library
heroku run "alembic upgrade dfdbdb2b7d7e" (upgrading to specific version) <br/>


### create a Procfile in root directory and add below line to start up the application
web: uvicorn api.main:app --host=0.0.0.0 --port=${PORT:-5000}

### Add postgres server in heroku: 
heroku addons:create heroku-postgresql:hobby-dev
### Add expected environment variables (config.py file) in heroku application settings
https://dashboard.heroku.com/apps/shyam-orders/settings (In my case)

### See application state
https://shyam-orders.herokuapp.com/

### See supported operations with below URL
https://shyam-orders.herokuapp.com/docs
