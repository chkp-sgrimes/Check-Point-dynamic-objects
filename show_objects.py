# import json
from utils.cp_client import CpClient


def main():
    objects: list[dict]
    client: object

    client = CpClient()
    res = client.login()
    res = client.get_all_objects(['host','network'])
    res = client.logout()


if __name__ == '__main__':
    main()
