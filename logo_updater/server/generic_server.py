from logo_updater.connection import create_ssh_connection, upload_files_with_scp
from scp import SCPClient
from tqdm import tqdm

class GenericServer:
    """
    This class implements a generic file upload to a linux server
    """
    def __init__(self, server_address: str, server_port: int, server_username: str, server_password: str):
        self.server_address = server_address
        self.server_port = server_port
        self.server_username = server_username
        self.server_password = server_password

    def update_logo_on_server(self, logo_filename: str):
        """
        This function updates the logo on a generic linux server
        """

        try:
            ssh_connection = create_ssh_connection(self.server_address, self.server_port, self.server_username, self.server_password)
        except Exception as ssh_exception:
            print(f"[-] An error with the SSH connection occurred: {ssh_exception}")
            return

        ssh_transport = ssh_connection.get_transport()
        scp_connection = SCPClient(ssh_transport)

        for remote_logo_path in tqdm(self.LOGO_PATHS_ON_SERVER):
            upload_files_with_scp(scp_connection, logo_filename, f"{remote_logo_path}/{self.LOGO_NAME_ON_SERVER}")

        scp_connection.close()
        ssh_connection.close()

        print(f"[+] Logo updated, visit http://{self.server_address}:{self.WEB_SERVER_PORT} to see it")


