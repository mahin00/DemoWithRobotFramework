import requests
import json
import dateutil.parser
import datetime
import csv
from os import path

global login_route, csrf_route, users_route, roles_route, session_obj, request_headers, base_url

request_headers = {'content-type': 'application/json'}
login_route = "/api/v1/login"
csrf_route = "/api/v1/csrf"
users_route = "/api/v1/users"
roles_route = "/api/v1/roles"
base_url = 'https://dev.alex4im.com:9443'
session_obj = requests.Session()

def login(username, password):
    login_url = base_url + login_route

    request_headers = {'content-type': 'application/json'}

    login_body = {
        "data": {
            "username": username,
            "password": password
        }
    }
    session_obj.post(login_url, data=json.dumps(login_body), headers=request_headers)

def get_response(users_url):
    users_body = {}
    csrf_headers = request_headers
    response = session_obj.get(users_url, data=json.dumps(users_body, indent=4, sort_keys=True), headers=csrf_headers).text
    parsed_json = json.loads(response)
    str = json.dumps(parsed_json[0], indent=4, sort_keys=True)
    str = json.loads(str)
    return str

def check_time(base_url, username, password):
    login(username, password)
    users_url = base_url + "/api/v1/import/jobs"

    parsed_json = get_response(users_url)

    old_date = parsed_json['date']
    old_date = dateutil.parser.parse(old_date)

    new_date = parsed_json['statistics']['date']
    new_date = dateutil.parser.parse(new_date)

    date_diff = (new_date-old_date).total_seconds()

    return date_diff

def store_results_into_csv(operation_type, time_taken, user_type, username, nfr):
    current_date_time = datetime.datetime.now()
    date = current_date_time.strftime("%d-%m-%Y")
    time = current_date_time.strftime("%H:%M:%S")

    if not path.exists('results.csv'):
        results = open('results.csv', mode='w')
        results = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        header_row = ['Date', 'Time', 'Operation Type', 'Time of Operation', 'User Type', 'Username', 'NFR']
        results.writerow(header_row)

    with open('results.csv', mode='a') as results:
        results = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        results.writerow([date, time, operation_type, time_taken, user_type, username, nfr])

def check_rollback_time(base_url, username, password):
    login(username, password)
    users_url = base_url + "/api/v1/import/jobs"
    parsed_json = get_response(users_url)

    rollback_url = base_url + "/api/v1/import/jobs/" + parsed_json['id'] + "/rollback"
    if parsed_json['status'] != 'ROLLED_BACK':
        session_obj.post(rollback_url, files=dict(job=parsed_json['id']))
        old_time = datetime.datetime.now()
        while parsed_json['status'] != 'ROLLED_BACK':
            parsed_json = get_response(users_url)
        new_time=datetime.datetime.now()
        time_diff = (new_time-old_time).total_seconds()
    return time_diff

def check_classification_time(base_url, username, password):
    login(username, password)
    classification_url = base_url + "/api/v1/classificationJob"
    parsed_json = get_classification(classification_url)

    length = len(parsed_json['classificationJobs'])-1
    id = parsed_json['classificationJobs'][length]['id']

    status = get_classification_status(id)
    if status == "In Progress":
        old_time = datetime.datetime.now()
        print("processing")
        while status != "Complete":
            status = get_classification_status(id)
        new_time=datetime.datetime.now()
        time_diff = (new_time-old_time).total_seconds()
    return time_diff

def get_classification(classification_url):
    classification_body = {}
    response = session_obj.get(classification_url, data=json.dumps(classification_body, indent=4, sort_keys=True), headers=request_headers).text
    parsed_json = json.loads(response)
    return parsed_json

def get_classification_status(id):
    status_url = base_url + "/api/v1/classificationJob/"+str(id)+"/status"
    response = session_obj.get(status_url, files=dict(id=id)).text
    return response