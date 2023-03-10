"""This module contains the Nornir task for GNMI Get() leveraging pygnmi"""
# Modules
from nornir.core.task import Task, Result


# Functions
def get_state(
    task: Task,
    prefix: str = "",
    yang_path: str = None,
    target: str = None,
    datatype: str = "all",
    encoding: str = "json",
) -> Result:
    """This task is based on Get() GNMI RPC.
    The RPC takes a number of inputs and reutrns dictionary of supported by a device capabilities.
    Also, the gNMIclient may need extra args.
    Check https://github.com/akarneliuk/pygnmi for further details"""

    pysros_conn = task.host.get_connection(
        connection="pysros", configuration=task.nornir.config
    )

    result = pysros_conn.running.get(yang_path, defaults=True)

    return Result(host=task.host, result=result, changed=False)
