from pchem.constants import *
import pchem.utils

from threading import Lock
import socket
import toml

CONFIG_PATH = "./config.toml"

# Singleton class of the TCP connection to Propsim. #
# Sends AT commands to Propsim and returns the Propsim response #
class PropsimSocket(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PropsimSocket, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        with open(CONFIG_PATH, 'r') as f:
            config = toml.load(f)
            self._propsim_ip = config['propsim']['ip']
            self._propsim_port = config['propsim']['port']
            self._propsim_lock = Lock()
            self._timeout = config['propsim']['timeout']

    def execute_at_command(self, at_command):
        try:
            # To-do: Read Propsim error register
            self._propsim_lock.acquire()
            propsim_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            propsim_connection.settimeout(self._timeout)
            propsim_connection.connect((self._propsim_ip, self._propsim_port))
            propsim_connection.sendall(at_command.encode("utf-8"))
            response = ""

            # Propsim will send a respond to a query. A query contains ? in the at_command string. Read this propsim response below.
            if "?" in at_command:
                while not "\n" in response:
                    response += propsim_connection.recv(1024).decode("utf-8")
                propsim_connection.close()
            
            pchem_response = pchem.utils.create_pchem_response(RESPONSE_STATUS.OK, "", response.strip())
        except Exception as e:
            pchem_response = pchem.utils.create_pchem_response(RESPONSE_STATUS.EXECUTION_ERROR, str(e))
        finally:
            self._propsim_lock.release() 
            return pchem_response
