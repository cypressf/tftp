#import UDPClient
#from TFTP import TFTP
class UDPClient: pass
class TFTP:
    def __init__(self):
        pass

    def ACK(self):
        pass

    def DATA(self, block, leftoverbytes, contents):
        pass

    def RQR(self, filename, mode):
        pass


class TFTPClient(TFTP):
    def __init__(self):
        print ("""
        TFTP Client.

        Enter help for help.

        """)
        self.commandtable = {
            "help":self.help,
            "ls":self.ls,
            "set_ip": self.set_ip,
            "cd": self.cd,
            "upload": self.upload,
            "download": self.download,
            "end":self.end
        }
        
        self.wd = "/usr"
        self.server_ip = None
        self.server_port = None
        self.running = True
        
        while self.running:
            self.userinput = input(""">>> """)

            cp  = self.userinput.strip(" ").split(" ")
            command, param = cp[0],cp[-1]

            if command in self.commandtable:
                self.runing = self.commandtable[command](param)
            else:
                print ("That's not a command.")

    def cd(self, wd):
        self.wd = wd.strip("'")
        return self.ls("")

    def ls(self, noparam):
        print(self.wd)

    def set_ip(self, IP):
        self.serverIP = IP
        print (self.serverIP)

    def end(self, noparam):
        self.running = False

    def upload(self, filename):
        """
        Send file from client to server.
        """
        TFTP_Address = (self.server_ip, self.server_port)

        with UDPclient() as sock, open(PlatformFilename,"R") as fd:

            sock.sendto(self.RQW(PlatformFilename), TFTP_Address)
            payload, ServerIPAddress = sock.recv(1024)

            filecontents = fd.read()
            filelen = len(filecontents)
            fullblockct, leftoverbytes = divmod(filelen,512)
            
            for block in range(fullblockct):
                self.DATA(block,filecontents[block*512,512])
                if not self.ACK(): raise TFTPErrorError
                
            self.DATA(block,
                      leftoverbytes,
                      filecontents[-leftoverbytes:])

            if not self.ACK():
                raise TFTPErrorError
                        
    def download(self, filename):
        """
        Send filename from TFTP client to TFTP server.
        """
        with UDPclient() as sock, open(PlatformFilename,"W") as fd:
                            
        #bug: we should test to be sure PlatformFilename's not there before we
        # write.  We really need a strict creat.

            self.RQR(filename)

            filecontents = bytearray([])
            block = self.Data()
            while 512 == len(block):
                filecontents.append(block)
                block = self.Data()
            filecontents.append(block) # the short block is the ACK

            fd.write(filecontents)

    def help(self, *param, **xdict):
        print ("""
ls                                     # >>> ls
                                        # usr/george/
set_ip    TCP.server.IP.address          # >>> set_ip  10.2.3.4 
                                        # 10.2.3.4  
cd       'path'                         # >>> cd '/projectb/'
                                        # /projectb/
upload   'filename'                     # >>> upload 'test.txt'
                                        # text.txt uploaded
download 'filename'                     # >>> download 'newtest.txt'
                                        # newtest.txt downloaded 
exit

>>> """)

TFTPClient()
        
