# Author: Eldad Izhaky
# Date: 02/01/2023
# Filename: main.py
# Purpose: Update the logo on a TwonkyMedia server

from logo_updater.server.twonky_server import TwonkyMediaServer
from logo_updater.logo_updater import update_logo_on_server
from logo_updater.exceptions import PasswordNotFound, UsernameNotFound
from typing import Tuple
import argparse
import os


TWONKY_SSH_PORT = 22
TWONKY_USERNAME_ENV_VARIABLE = "TWONKY_USERNAME"
TWONKY_PASSWORD_ENV_VARIABLE = "TWONKY_PASSWORD"


def get_arguments() -> argparse.Namespace:
    """
    This function returns an object that contains the arguments for the program
    """

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("server_address", type=str, help="The address to the server")
    argument_parser.add_argument("filename", type=str, help="The path to the file to upload")
    argument_parser.add_argument("-p", "--port", type=int, nargs="?", help="The port of the server", const=1, default=TWONKY_SSH_PORT)
    return argument_parser.parse_args()


def get_credentials_from_environment_variables() -> Tuple[str, str]:
    """
    This function returns a tuple that contains the credentials of the SSH user.
    """

    twonky_username = os.getenv(TWONKY_USERNAME_ENV_VARIABLE)
    if not twonky_username:
        print(f"[-] Username not found, please set the {TWONKY_USERNAME_ENV_VARIABLE} env variable using export")
        raise UsernameNotFound

    twonky_password = os.getenv(TWONKY_PASSWORD_ENV_VARIABLE)
    if not twonky_password:
        print(f"[-] Password not found, please set the {TWONKY_PASSWORD_ENV_VARIABLE} env variable using export")
        raise PasswordNotFound

    return twonky_username, twonky_password


def main():
    """
    This function creates a connection to the server and updates the logo
    """

    program_arguments = get_arguments()

    try:
        twonky_username, twonky_password = get_credentials_from_environment_variables()
    except Exception:
        return

    update_logo_on_server(
        server_class=TwonkyMediaServer,
        server_address=program_arguments.server_address,
        server_port=program_arguments.port,
        server_username=twonky_username,
        server_password=twonky_password,
        logo_filename=program_arguments.filename)


if __name__ == "__main__":
    main()
