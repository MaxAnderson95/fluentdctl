import fire
import requests
from enum import Enum

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 24444


class Command_Type(Enum):
    FLUSH = 1
    STOP = 2
    FLUSHTHENSTOP = 3
    RELOAD = 4


COMMAND_MAP = {
    1: "plugins.flushBuffers",
    2: "processes.killWorkers",
    3: "processes.flushBuffersAndKillWorkers",
    4: "config.gracefulReload"
}


def execute_command(host, port, command, verbose):
    command_text = COMMAND_MAP.get(command.value)
    url = f"http://{host}:{port}/api/{command_text}"

    if verbose:
        print(
            f"Performing command '{command_text}' against host '{host}' on port '{port}'. Raw URL: {url}")

    try:
        r = requests.get(url)
    except requests.exceptions.HTTPError:
        return "Error: HTTP error occured"
    except requests.exceptions.ConnectionError:
        return "Error: Target machine could not be reached or it actively refused the connection."
    except requests.exceptions.Timeout:
        return "Error: Timeout error"
    except requests.exceptions.RequestException:
        return "Error: Unknown error occured"

    json = r.json()
    if json.get("ok") != True:
        return json
    elif verbose:
        return f"Command executed successfully. Raw output: '{json}'"
    else:
        pass


def command_factory(command_type):
    def command(host: str = DEFAULT_HOST, port: int = DEFAULT_PORT, verbose: bool = False):
        return execute_command(host, port, command_type, verbose)
    return command


def main():
    fire.Fire({
        "flush":         command_factory(Command_Type.FLUSH),
        "stop":          command_factory(Command_Type.STOP),
        "flushthenstop": command_factory(Command_Type.FLUSHTHENSTOP),
        "reload":        command_factory(Command_Type.RELOAD)
    })


if __name__ == "__main__":
    main()
