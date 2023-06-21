import json
from utils.cp_client import CpClient


# def readrules() -> list[dict]:
#     with open('./inputs/rules.json', 'r') as f:
#         data = json.load(f)
#         return data['rules']


def read_json(jsonfile: str) -> list[dict]:
    """
    Reads a json file and returns a list of dictionaries.
    """
    try:
        with open('./inputs/' + jsonfile, 'r') as f:
            data = json.load(f)
            return data['objects']
    except:
        print("Error reading json file")


def main():
    cp_client: object
    objs: list[dict]

    objs = read_json("objects.json")
    cp_client = CpClient()
    cp_client.login()
    cp_client.add_objects(objs)
    cp_client.publish()
    cp_client.logout()


if __name__ == '__main__':
    main()
