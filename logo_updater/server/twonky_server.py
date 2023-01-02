from logo_updater.server.generic_server import GenericServer

class TwonkyMediaServer(GenericServer):
    """
    This class implements the TwonkyMedia server 
    """

    LOGO_PATHS_ON_SERVER = [
        "/mnt/ext/opt/twonkymedia/resources/webbrowse",
        "/mnt/ext/opt/twonkymedia/resources/webconfig",
        "/share/CACHEDEV2_DATA/.qpkg/TwonkyServer/resources/webbrowse",
        "/share/CACHEDEV2_DATA/.qpkg/TwonkyServer/resources/webconfig"
    ]
    LOGO_NAME_ON_SERVER = "logo_twonky.gif"
    WEB_SERVER_PORT = 9000

    def __init__(self, server_address: str, server_port: int, server_username: str, server_password: str):
        super().__init__(server_address, server_port, server_username, server_password)
