from paramiko import SSHClient
from scp import SCPClient

def create_ssh_connection(server_address: str, server_port: int, server_username: str, server_password: str) -> SSHClient:
    """
    Creates an SSH connection object from the given parameters
    """

    ssh_connection = SSHClient()
    ssh_connection.load_system_host_keys()

    ssh_connection.connect(
        hostname=server_address,
        port=server_port,
        username=server_username,
        password=server_password
        )
    return ssh_connection

def upload_files_with_scp(scp_connection: SCPClient, local_file_path: str, remote_file_path: str):
    """
    This function uploads a given filename to a given path in the remote server using a SCP client
    """

    scp_connection.put(local_file_path, remote_file_path)
