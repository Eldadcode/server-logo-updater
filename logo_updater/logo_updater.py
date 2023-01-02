from logo_updater.server.generic_server import GenericServer
import os


def update_logo_on_server(server_class: GenericServer, server_address: str, server_port: int, server_username: str, server_password: str, logo_filename: str):

    server_instance = server_class(server_address, server_port, server_username, server_password)
    if not os.path.exists(logo_filename):
        print(f"[-] {logo_filename} is not a valid file")
        raise FileNotFoundError

    server_instance.update_logo_on_server(logo_filename)
