# import json
from cpapi import APIClient, APIClientArgs
from utils.cpobject_exporter


def do():
    api_response = []

    client_args = APIClientArgs(server='172.16.1.1')
    # password = getpass.getpass("Enter password:")

    with APIClient(client_args) as client:
        try:
            # other password approaches include bcrypt encrypted file, and keychain package
            api_response = client.login('admin', 'vpn123')
            print({'request': 'login', 'status_code': api_response.status_code})
        except TypeError:
            print("Login error occurred")
            return None

def load_endpoints():
    pass

def main():
    pass



if __name__ == '__main__'
    main()