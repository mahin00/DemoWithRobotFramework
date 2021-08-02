import requests
import json

class RobotEnvironmentSetup(object):

    global login_route, csrf_route, users_route, roles_route, reset_temp_pw_route

    login_route = "/api/v1/login"
    csrf_route = "/api/v1/csrf"
    users_route = "/api/v1/users"
    roles_route = "/api/v1/roles"
    reset_temp_pw_route = "/resetTemporaryPassword"

    # currently unused function, to be uplifted in the future
    def reset_temporary_password_internal(self, users, password, base_url):
        global reset_temp_pw_route

        reset_temp_pw_url = base_url + reset_temp_pw_route
        users_url = base_url + users_route

        for u in users:
            (session_obj, csrf_headers) = self.get_header_with_csrf_token(u, password, base_url)

            reset_temp_pw_body = {
                "user": {
                    "username": u,
                    "firstName": '',
                    "lastName": '',
                    "email": '',
                    "phone": '',
                    "enabled": True,
                    "authProvider": "local"
                },
                "initialPassword": password,
                "emailPasswordToUser": True
            }

            # create user
            session_obj.post(reset_temp_pw_url, data=json.dumps(reset_temp_pw_body), headers=csrf_headers)

        return

    '''
        returns (session_obj, csrf_headers, error_message)
    '''
    @staticmethod
    def get_header_with_csrf_token(admin_username, admin_password, base_url):
        global login_route, csrf_route

        login_url = base_url + login_route
        csrf_url = base_url + csrf_route

        request_headers = {'content-type': 'application/json'}
        session_obj = requests.Session()

        login_body = {
            "data": {
                "username": admin_username,
                "password": admin_password
            }
        }

        # login
        login_response = session_obj.post(login_url, data=json.dumps(login_body), headers=request_headers)

        if (login_response.status_code != 200):
            return (session_obj, None, "login failed, login_response.status_code: " + login_response.status_code)

        # get csrf token
        csrf_response = session_obj.get(csrf_url, headers=request_headers)

        if (csrf_response.status_code == 200):
            csrf_headers = request_headers
            csrf_headers["X-CSRF-Token"] = csrf_response.json()['csrf-token']
            
            return (session_obj, csrf_headers, None)

        elif (csrf_response.status_code == 404):
            return (session_obj, None, "csrf not enabled")

        else:
            return (session_obj, None, "unknown failure, csrf_response.status_code: " + csrf_response.status_code)

    '''
        returns create_users_success_failure
    '''
    @staticmethod
    def create_users_helper(users, session_obj, create_user_headers, admin_password, base_url):
        global users_route

        users_url = base_url + users_route
        
        for u in users:
            users_body = {
                "user": {
                    "username": u,
                    "firstName": '',
                    "lastName": '',
                    "email": '',
                    "phone": '',
                    "enabled": True,
                    "authProvider": "local"
                },
                "initialPassword": admin_password,
                "emailPasswordToUser": True
            }

            # create user
            create_user_response = session_obj.post(users_url, data=json.dumps(users_body), headers=create_user_headers)

            if (create_user_response.status_code != 200):
                return "failed to create user " + u

        return "Success"

    '''
        returns error message or create_users_success_failure
    '''
    def create_users_v1_api(self, admin_username, admin_password, users, base_url):
        (session_obj, csrf_headers, error_message) = self.get_header_with_csrf_token(admin_username, admin_password, base_url)

        if (error_message):
            return error_message
        
        create_users_success_failure = self.create_users_helper(users, session_obj, csrf_headers, admin_password, base_url)

        return create_users_success_failure

    '''
        returns error message or assign_users_to_admin_role_success_failure
    '''
    def assign_user_to_admin_v1_api(self, admin_username, admin_password, default_admin_role, users, base_url):
        global users_route, roles_route

        users_url = base_url + users_route
        roles_url = base_url + roles_route

        (session_obj, csrf_headers, error_message) = self.get_header_with_csrf_token(admin_username, admin_password, base_url)

        if (error_message):
            return error_message

        admin_role_id = -100

        # get the id of the admin role
        all_roles = session_obj.get(roles_url, headers=csrf_headers).json()

        for role in all_roles:
            if role["name"] == default_admin_role:
                admin_role_id = role["id"]

        # get the ids of the users
        all_users = session_obj.get(users_url, headers=csrf_headers).json()

        all_ids = []

        for usr in all_users:
            if usr["username"] in users:
                all_ids.append(usr["id"])

        for usr_id in all_ids:

            url_to_use = roles_url
            url_to_use += "/"
            url_to_use += str(admin_role_id)
            url_to_use += "/members/users/"
            url_to_use += str(usr_id)

            # assign the user to the role
            resp = session_obj.post(url_to_use, data=json.dumps({}), headers=csrf_headers)

            if (resp.status_code != 200):
                return "failed to assign user " + usr_id + " to role admin"

        return "Success"
