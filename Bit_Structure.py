class Bit_structure():
    def __init__(self):
        self.transmit_field_offset = 0

    def register(self, bit_field_type):

        specified_bdf_offset, bdf_type = arg_bit_data_field

        _offset = self.bit_field_offset

        if predicted_bdf_offset != calculated_bdf_offset:
            raise ValueError(
                "Bit Data Field offset error:\n"+\
                "Predicted %n, Calculated %n"%predicted_offset,calculated_offset)

        self.bit_field_offset  +=  bfd_type.length
        self.bit_fields.append( Bit_Data_Field(self.bit_field_type,length) )


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
    def __init(self, number):
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
    def __init__(self, message_string):
        self.message_string = message_string
        self.offset = 8 * len(message_string)

    def __str__(self):
        return self.message_string
