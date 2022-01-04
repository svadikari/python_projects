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



## Run Application Server

uvicorn api.main:app --reload


## Deploy to Heroku 
Create an account in heroku.com

Login: heroku login <br/>
Clone the repo: heroku git:clone -a shyam-orders <br/>
cd shyam-orders <br/>
git add . <br/>
git commit -am "initial commit" <br/>
git push heroku master <br/>
heroku logs --tail <br/>

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
