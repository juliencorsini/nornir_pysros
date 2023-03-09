"""This is a plugin to establish a long-living connectivity
to a network device via Pysros"""
# Modules
from typing import Optional, Any, Dict
from nornir.core.configuration import Config
from pysros.management import connect


# Classes
class PysrosNornirConnectionPlugin:
    """This class creates a long-term connectivity to network device via Netconf
    using pysros library"""

    def open(
        self,
        hostname: Optional[str],
        username: Optional[str],
        password: Optional[str],
        key_filename: Optional[str],
        port: Optional[int],
        platform: Optional[str],
        extras: Optional[Dict[str, Any]] = None,
        configuration: Optional[Config] = None,
    ) -> None:
        """Method to open the pysros connectivity"""
        # Ditch variables which are not used at the moment
        _ = platform
        _ = configuration

        connection = connect(
            target=(hostname, port),
            username=username,
            password=password,
            key_filename=key_filename,
            **extras
        )
        connection.connect()
        self.connection = connection

    def close(self) -> None:
        """Method to close the pysros connectivity"""
        self.connection.close()
