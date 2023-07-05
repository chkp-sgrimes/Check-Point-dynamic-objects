from cpapi import APIClientArgs
from cpapi import APIClient


# from itertools import chain


class CpClient:

    def __init__(self):
        self.response = None
        self.client_args = None
        self.client = None

    def login(self) -> None:
        self.client_args = APIClientArgs(server='172.16.1.1')
        self.client = APIClient(self.client_args)
        # options for passwords
        # python vault
        # save as environment variable
        # in .env file that is not part of git config
        # getpass
        # response = self.client.login("otto", "mation4ever")
        response = self.client.login("otto", "mation4ever")
        print(response)
        # self.response = self.client.login("admin", "vpn123")

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

    def gen_api_command(self, command: str, payload=None) -> list[dict]:

        try:
            response = self.client.gen_api_query(command, payload=payload)
            if response.gi_code.co_argcount > 0:
                print(f"successfully executed {command}")
                # return response
            else:
                raise Exception(response)
        except Exception as e:
            print(e)

        return response

    def show_rulebase(self):
        pass

    def add_objects(self, objs: list[dict], res_hander: object) -> list[dict]:
        payload: dict
        command: str
        o: dict

        for o in objs:
            # old method of checking before RequestChecker
            # response = self.api_command("where-used", {"name": objs["name"]})
            # if response.data['used-directly']['total'] > 0:
            #     return response
            # else:
            #     command = "add-" + o["object-type"]
            command = "add-" + o["object-type"]

            # payload as dict.  updatable objects are created with uid-in-updatable-objects-repository
            # rather than a name
            if command == "add-updatable-object":
                payload = {key: val for key, val in o.items() if key == "uid-in-updatable-objects-repository"}
            else:
                payload = {key: val for key, val in o.items() if key != "object-type"}
                response = self.api_command(command, payload)
                # response = res_hander.parse_response(response)
        return response

    def where_used(self, ):
        pass

    def delete_objects(self, objs: list[dict]) -> list[dict] :
        payload: dict
        command: str
        o: dict

        for o in objs:
            # old method of checking before RequestChecker
            # check if the object is used and cannot be deleted
            # response = self.api_command("where-used", {"name": objs["name"]})
            # if response.data['used-directly']['total'] > 0:
            #     return response
            # else:
            #     command = "delete-" + o["object-type"]
            command = "delete-" + o["object-type"]
            # payload as dict.  need only the name to delete
            payload = {key: val for key, val in o.items() if key == "name"}
            response = self.api_command(command, payload)
        return response

    def get_all_objects(self, types: list) -> list[dict]:
        # all_gens = chain()
        gens = []
        result_gen: None

        for target in types:
            result_gen = self.gen_api_command("show-objects", payload={"type": target})
            try:
                print(next(result_gen))
            except StopIteration:
                pass
            gens.append({"type": target, "objects": result_gen})
        return gens

    def rules(self):
        pass
