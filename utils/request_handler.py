class RequestChecker:

    def __init__(self, cl) -> None:
        self.cl = cl
        pass

    def check_object_action(self, action):
        allowed_actions = ['delete', 'set', 'add', 'show', 'clone']
        # updatable objects do not have clone
        # network feeds also have a check
        pass

    def check_objects(self, original_manifest: list[dict], action="add") -> list[dict]:
        new_manifest: list[dict] = []
        rejected_manifest: list[dict] = []
        obj: dict

        for obj in original_manifest:
            name = obj["name"]
            used_in_rules = False

            response = self.cl.api_command("where-used", {"name": name})
            # if object does not exist response is None
            # if object exists response.status_code is 200

            # is the object used in any rules?
            if response is not None:
                used_in_rules = len(response.data['used-directly']['access-control-rules']) | \
                                len(response.data['used-directly']['threat-prevention-rules']) | \
                                len(response.data['used-directly']['nat-rules']) | \
                                len(response.data['used-directly']['https-rules'])

            match action:
                case 'add' if response is not None:
                    rejected_manifest.append(obj)
                case 'add' if response is None:
                    new_manifest.append(obj)
                case 'delete' if used_in_rules:
                    rejected_manifest.append(obj)
                case 'delete' if not used_in_rules:
                    new_manifest.append(obj)
                case _:
                    new_manifest.append(obj)

        # log rejected manifest

        return new_manifest

    def check_rules(self):
        pass
