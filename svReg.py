class Field:
    def __init__(self, name, size, lsb_pos, access, reset):
        self.name = name
        self.size = size
        self.lsb_pos = lsb_pos
        self.access = access
        self.reset = reset

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_lsb_pos(self, lsb_pos):
        self.lsb_pos = lsb_pos

    def get_lsb_pos(self):
        return self.lsb_pos

    def set_access(self, access):
        self.access = access

    def get_access(self):
        return self.access

    def set_reset(self, reset):
        self.reset = reset

    def get_reset(self):
        return self.reset


class Field_Trim(Field):
    def __init__(
        self, name, size, lsb_pos, access, reset, portenable=False, inverted=False
    ):
        super().__init__(name, size, lsb_pos, access, reset)
        self.portenable = portenable
        self.inverted = inverted

    def set_portenable(self, portenable):
        self.portenable = portenable

    def get_portenable(self):
        return self.portenable

    def set_inverted(self, inverted):
        self.inverted = inverted

    def get_inverted(self):
        return self.inverted


class Reg:
    def __init__(self, name=None, address=None):
        self.name = name
        self.address = address
        self.fields = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def add_field(self, field):
        if isinstance(field, Field):
            self.fields.append(field)
        else:
            raise TypeError("Expected a Field instance")

    def get_fields(self):
        return self.fields

    def get_field_by_name(self, name):
        for field in self.fields:
            if field.get_name() == name:
                return field
        return None

    def remove_field(self, name):
        for i, field in enumerate(self.fields):
            if field.get_name() == name:
                del self.fields[i]
                return True
        return False

    def __str__(self):
        fields_str = ", ".join(
            [f"{field.get_name()}({field.get_size()})" for field in self.fields]
        )
        return f"Reg(name={self.name}, address={self.address}, fields=[{fields_str}])"

    def __repr__(self):
        return self.__str__()


class Reg_Trim(Reg):

    def __init__(self, name=None, address=None, memory_address=None):
        self.memory_address = memory_address
        super().__init__(name, address)

    def set_memory_address(self, memory_address):
        self.memory_address = memory_address

    def get_memory_address(self):
        return self.memory_address

    def add_field(self, field):
        return super().add_field(field)
