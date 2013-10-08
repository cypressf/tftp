import socket
import threading

class TFTP(socket.socket):

    def __init__(self, timeout=2.0, address=("0.0.0.0", 5000)):
        """
        Create the socket, bind to the address, and set timeout to the timeout.
        """
        super().__init__(socket.AF_INET, socket.SOCK_DGRAM)
        self.settimeout(2.0)
        self.bind(address)

    def received_ack(self, block_number):
        while True:
            try:
                raw_data = self.recv(1024)
                data = raw_data.decode('UTF-8')
            except self.timeout:
                return False

    def ack(self, block_number):
        pass

    def data(self, block_number, data):
        pass

    def rrq(self, filename, mode):
        pass

    def wrq(self, filename, mode):
        pass

    def error(self, error_code, error_message):
        pass

    def __del__(self):
        self.running = False
        try:
            self.sock.close()
        except socket.error as e:
            print(e)
