from cpapi import APIClientArgs
from cpapi import APIClient
# from itertools import chain


class CpClient:

    def __init__(self):
        self.response = None
        self.client_args = None
        self.client = None
        self.session = None

    def login(self) -> None:
        self.client_args = APIClientArgs(server='172.16.1.1')
        self.client = APIClient(self.client_args)
        self.response = self.client.login("admin", "vpn123")

    def logout(self) -> list[dict]:
        self.response = self.client.api_call("logout")
        return self.response

    def publish(self):
        self.response = self.client.api_call("publish")

    def api_command(self, command: str, payload=None) -> list[dict]:

        try:
            response = self.client.api_call(command, payload)
            if response.status_code > 200:
                raise Exception(response)
            else:
                print(f"command:{command}\n{response}")
                return response
        except Exception as e:
            print(f"command:{command}\n{e}")
            return e

    def gen_api_command(self, command: str, payload=None) -> list[dict]:

        try:
            response = self.client.gen_api_query(command, payload=payload)
            if response.gi_code.co_argcount > 0:
                print(f"successfully executed {command}")
                return response
            else:
                raise Exception(response)
        except Exception as e:
            print(e)
            return response

    def show_rulebase(self):
        pass
        # self.response = self.client.api_call("show-access-rulebase", {"name": "Network"})
        # g = self.client.api_query("show-access-rulebase", payload={"name": "Network"})
        # print(self.response)
        # return None

    def add_objects(self, objs: list[dict]) -> None:
        payload: dict
        command: str
        o: dict

        for o in objs:
            command = "add-" + o["object-type"]

            # payload as dict.  updatable object are different
            if command == "add-updatable-object":
                payload = {key: val for key, val in o.items() if key == "uid-in-updatable-objects-repository"}
            else:
                payload = {key: val for key, val in o.items() if key != "object-type"}
            self.response = self.api_command(command, payload)
        return None

    def del_objects(self, objs: list[dict]) -> None:
        payload: dict
        command: str
        o: dict

        for o in objs:
            command = "delete-" + o["object-type"]

            # payload as dict.  need only the name to delete
            payload = {key: val for key, val in o.items() if key == "name"}
            self.response = self.api_command(command, payload)
        return None

    def get_all_objects(self) -> list[dict]:
        target_objs = ['network', 'host']
        # all_gens = chain()
        gens = []
        result_gen: None

        for target in target_objs:
            result_gen = self.gen_api_command("show-objects", payload={"type": target})
            try:
                print(next(result_gen))
            except StopIteration:
                pass
            gens.append({"type": target, "objects": result_gen})
        return gens

    def rules(self):
        pass
