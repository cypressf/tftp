from TFTP import TFTP

class TFTPServer:
    def __init__(self):
        pass

    def run(self):
        with TFTP(address=("0.0.0.0", 5001)) as tftp:
            while True:
                try:
                    raw_message, address = tftp.recvfrom(1024)
                    message = raw_message.decode('UTF-8')
                except tftp.timeout:
                    continue
                except tftp.error as e:
                    print(e)
                    break
                except KeyboardInterrupt:
                    print("\nI can see when I\'m not wanted.")
                    break

if __name__ == "__main__":
    TFTPServer().run()
