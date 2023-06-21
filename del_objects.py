import json
from utils.cp_client import CpClient


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
    """
    Main function.
    """
    objects: list[dict]
    client: object

    client = CpClient()
    objects = read_json('objects.json')
    client.login()
    client.del_objects(objects)
    client.publish()
    client.logout()


if __name__ == '__main__':
    main()
