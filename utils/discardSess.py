from cpapi import APIClient, APIClientArgs


def main():

    client_args = APIClientArgs(server='172.16.1.1')

    with APIClient(client_args) as client:

        # The API client, would look for the server's certificate SHA1 fingerprint in a file.
        # If the fingerprint is not found on the file, it will ask the user if he accepts the server's fingerprint.
        # In case the user does not accept the fingerprint, exit the program.
        if client.check_fingerprint() is False:
            print("Could not get the server's fingerprint - Check connectivity with the server.")
            exit(1)

        # login to server:
        login_res = client.login("admin", "vpn123")

        if login_res.success is False:
            print("Login failed:\n{}".format(login_res.error_message))
            exit(1)

        show_sessions_res = client.api_query("show-sessions", "full")

        if not show_sessions_res.success:
            print("Failed to retrieve the sessions")
            return

        for sessionObj in show_sessions_res.data:
            # Ignore sessions that were not created with WEB APIs or CLI
            if sessionObj["application"] != "WEB_API":
                continue

            discard_res = client.api_call("discard", {"uid": sessionObj['uid']})
            if discard_res.success:
                print("Session '{}' discarded successfully".format(sessionObj['uid']))
            else:
                print("Session '{}' failed to discard".format(sessionObj['uid']))


if __name__ == "__main__":
    main()