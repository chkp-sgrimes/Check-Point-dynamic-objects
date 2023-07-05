import json
from utils.cp_client import CpClient
from utils.request_handler import RequestChecker


def read_json(jsonfile: str) -> list[dict]:
    """
    Reads a json file and returns a list of dictionaries.
    """
    try:
        with open('./inputs/' + jsonfile, 'r') as f:
            data = json.load(f)
            return data['objects']
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        print(f"Error {e}")


def main():
    objs = read_json("objects.json")

    cp_client = CpClient()
    cp_client.login()

    checker = RequestChecker(cp_client)
    corrected_objects = checker.check_objects(objs, "delete")
    cp_client.delete_objects(corrected_objects)
    # cp_client.publish()
    cp_client.logout()


if __name__ == '__main__':
    main()
