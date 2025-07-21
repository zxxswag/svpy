class svPort:
    def __init__(
        self,
        name: str,
        size: int,
        direction: str,
        datatype: str = "wire",
        description: str = "",
    ):
        self.name = name  # the name of the port
        self.direction = direction  # the direction of the port
        self.size = size  # the size of the port
        self.lsb = 0  # the least significant bit of the port, default is 0
        self.msb = size - 1  # the most significant bit of the port
        self.msb_alias_name = None
        self.lsb_alias_name = None
        self.datatype = datatype  # the data type of the port
        # the signedness of the port, default is 'unsigned', other is 'signed'
        self.signedness = "unsigned"
        self.description = description  # description of the port

    def __str__(self):
        return f"Port(name={self.name}, size={self.size}, direction={self.direction}, signedness={self.signedness})"

    def set_name(self, name):
        self.name = name

    def set_direction(self, direction):
        if direction not in ["input", "output", "inout", "ref"]:
            raise ValueError("Direction must be 'input', 'output', 'inout', or 'ref'.")
        self.direction = direction

    def set_size(self, size):
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Size must be a positive integer.")
        self.size = size

    def set_lsb(self, lsb):
        if not isinstance(lsb, int):
            raise ValueError("LSB must be an integer.")
        if lsb < 0:
            raise ValueError("LSB must be a non-negative integer.")
        self.lsb = lsb

    def set_msb(self, msb):
        if not isinstance(msb, int):
            raise ValueError("MSB must be an integer.")
        if msb < 0:
            raise ValueError("MSB must be a non-negative integer.")
        self.msb = msb

    def set_msb_alias_name(self, msb_alias_name):
        if not isinstance(msb_alias_name, str):
            raise ValueError("MSB alias name must be a string.")
        self.msb_alias_name = msb_alias_name

    def set_lsb_alias_name(self, lsb_alias_name):
        if not isinstance(lsb_alias_name, str):
            raise ValueError("LSB alias name must be a string.")
        self.lsb_alias_name = lsb_alias_name

    def set_datatype(self, datatype):
        if datatype not in ["wire", "reg"]:
            raise ValueError("Datatype must be 'wire' or 'reg'.")
        self.datatype = datatype

    def set_signedness(self, signedness):
        if signedness not in ["signed", "unsigned"]:
            raise ValueError("Signedness must be 'signed' or 'unsigned'.")
        self.signedness = signedness

    def set_description(self, description):
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
        self.description = description

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_direction(self):
        return self.direction

    def get_datatype(self):
        return self.datatype

    def get_signedness(self):
        return self.signedness

    def get_description(self):
        return self.description
