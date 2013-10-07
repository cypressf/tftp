class Bit_structure():
    def __init__(self):
        self.offset = 0
        self.bit_field_list = []

    def register(self, bit_field_type):
        self.offset += bit_field_type.offset
        self.bit_fild_list.append(bit_field_type)

class Bit_field_type():
    def __init__(self): raise NotImplemented
    def __eq__  (self, other): raise NotImplemented
    def __le__  (self, other): raise NotImplemented
    def __len__ (self): raise NotImplemented
    def __repr__(self): raise NotImplemented
    def __inv__ (self): raise NotImplemented
    def __or__  (self, other): raise NotImplemented
    def __and__ (self, other): raise NotImplemented
    def __xor__ (self, other): raise NotImplemented
    def __add__ (self, other): raise NotImplemented
    def __sub__ (self, other): raise NotImplemented
    def __str__ (self): raise NotImplemented


class Bit_field_bit(Bit_field_type):
    def __init__(self, identifier):
        self.identifier = identifier

class Bit_field_netascii(Bit_field_type):
    pass

class Opcode(Bit_field_type):
    def __init__(self, number):
        self.offset = 16
        self.strings = [
        "1     Read request (RRQ)"
        "2     Write request (WRQ)"
        "3     Data (DATA)"
        "4     Acknowledgment (ACK)"
        "5     Error (ERROR)"]

    def __eq__(self, other):
        return self.number == other.number

    def __str__(self):
        return self.strings[self.number + 1]

class ErrorCode(Bit_field_type):
    def __init__(self, number):
        self.offset = 16
        self.number = number
        self.strings = [
        "0         Not defined, see error message (if any).",
        "1         File not found.",
        "2         Access violation.",
        "3         Disk full or allocation exceeded.",
        "4         Illegal TFTP operation.",
        "5         Unknown transfer ID.",
        "6         File already exists.",
        "7         No such user."]

    def __eq__(self, other):
        return self.number == other.number

    def __str__(self):
        return self.strings[self.number]

class ErrMsg(Bit_field_type):
    def __init__(self, message_string=""):
        self.message_string = message_string
        # space for the message string + an extra byte for the null terminator
        self.offset = 8 * len(message_string) + 8

    def __str__(self):
        return self.message_string
