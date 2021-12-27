# test
test

pipenv shell
py manage.py runserver


Python code for api:

import requests
username = 'Shuhrat'
password = '1234567'
base_url = 'http://127.0.0.1:8000/api/'
# retrieve all courses
r = requests.get(f'{base_url}surveys/')
surveys = r.json()
available_surveys = ', '.join([survey['title'] for survey in surveys])
print(f'Available surveys: {available_surveys}')
