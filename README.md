# Car sell platform
Using Python 3.7.0
## Instalation
Create new folder, cd into it and create new virtualenv
```
virtualenv env --python=<path-to-python3>
source env/bin/activate
```
Clone the repository from

```
https://github.com/drion/cars-sp-python.git
```

cd to folder and add the .env file with SECRET_KEY to cars_sell_platform folder

```
SECRET_KEY = 'your-secret-key'
```
after that make install requirements
```
pip install -r requirements.txt
```
run migrations
```
./manage.py migrate
```
load fixtures
```
./manage.py loaddata cars.json
```
run server
```
./manage.py runserver
```