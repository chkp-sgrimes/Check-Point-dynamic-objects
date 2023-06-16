from cpapi import APIClientArgs
from cpapi import APIClient
from itertools import chain


class cpClient:

    def __init__(self):
        self.response = None
        self.user = "admin"
        self.password = "vpn123"
        self.client_args = None
        self.client = None
        self.session = None

    def login(self) -> None:
        self.client_args = APIClientArgs(server='172.16.1.1')
        self.client = APIClient(self.client_args)
        # self.client.login(self,"admin", "vpn123")
        self.response = self.client.login("admin", "vpn123")

        print("end")
        # with APIClient(client_args) as self.client:
        #     try:
        #         # other password approaches include bcrypt encrypted file, and keychain package
        #         self.response = self.client.login(self.user, self.password)
        #         # response = client.login("admin", "vpn123")
        #         print({'request': 'login', 'status_code': self.response.status_code})
        #         return None
        #     except TypeError:
        #         print("Login error occurred")
        #         return None

    def logout(self):
        self.response = self.client.api_call("logout")
        return None

    def publish(self):
        self.response = self.client.api_call("publish")

    def command(self) -> None:
        pass

    def show_rulebase(self):
        self.response = self.client.api_call("show-access-rulebase", {"name": "Network"})
        g = self.client.api_query("show-access-rulebase", payload={"name": "Network"})
        print(self.response)
        return None

    def add_objects(self, objs: list[dict]) -> None:
        payload: dict
        command: str
        o: dict

        for o in objs:
            command = "add-" + o["object-type"]

            # payload as string
            # payload = str({key: val for key, val in o.items() if key != "type"})

            # payload as dict
            payload = {key: val for key, val in o.items() if key != "object-type"}
            self.response = self.client.api_call(command, payload)
        # self.response = self.client.api_call(command, payload)
        return None

    def get_all_objects(self):
        target_objs = ['network', 'host']
        all_gens = chain()

        for target in target_objs:
            result_gen = self.client.gen_api_query("show-objects", details_level="full", payload={"type": target})
            all_gens = chain(all_gens, result_gen)

        return all_gens

    def rules(self):
        pass
