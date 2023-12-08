import socket
import toml
from threading import Lock

CONFIG_PATH = "./config.toml"

# Singleton class of the TCP connection to Propsim. #
# Sends AT commands to Propsim and returns the response #
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

    def execute_at_command(self, at_command):
        try:
            self._propsim_lock.acquire()
            propsim_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            propsim_connection.connect((self._propsim_ip, self._propsim_port))
            propsim_connection.sendall(at_command.encode("utf-8"))
            response = ""
            while not "\n" in response:
                response += propsim_connection.recv(1024).decode("utf-8")
            propsim_connection.close()
            response = response.strip()
        except Exception as e:
            response = str(e)
        finally:
            self._propsim_lock.release() 
            return response