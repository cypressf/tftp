from TFTP import TFTP

class TFTPClient:

    def __init__(self):
        pass

    def upload(self, filename, address):
        """
        Request to write a file (and request connection). If approved, write the file.

        If not approved, just return False.
        """
        with TFTP() as tftp, open(filename,"R") as fd:

            # parse file into blocks
            file_contents = fd.read()
            file_length = len(file_contents)
            block_count, leftover_bytes = divmod(file_length, 512)
            
            # ask to write
            tftp.sendto(tftp.wrq(filename), address)
            while not received_ack(0):
                tftp.sendto(tftp.wrq(filename), address)

            # write the file
            for block_number in range(block_count):
                start_index = block_number * 512
                end_index = start_index + 512
                data = tftp.data(block_number, file_contents[start_index:end_index])
                
                tftp.sendto(data, address)

                while not received_ack(block_number + 1):
                    tftp.sendto(data, address)
                
            # write the last block of the file (it's probably not a full 512 bytes)
            data = tftp.data(block, leftoverbytes, filecontents[-leftoverbytes:])
            tftp.sendto(data, address)
            while not received_ack(block_count + 1):
                tftp.sendto(data, address)


    def download(self, filename, address):
        """
        Send filename from TFTP client to TFTP server.
        """
        # with UDPclient() as udp_client, open(filename,"W") as fd:

        # #bug: we should test to be sure filename's not there before we
        # # write.  We really need a strict creat.

        #     tftp.RQR(filename)

        #     filecontents = bytearray([])
        #     block = tftp.data()
        #     while 512 == len(block):
        #         filecontents.append(block)
        #         block = tftp.data()
        #     filecontents.append(block) # the short block is the ACK

        #     fd.write(filecontents)
        pass        
