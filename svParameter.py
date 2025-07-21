class svParameter:
    def __init__(self, name, value, description=""):
        self.name = name  # the name of the parameter
        self.value = value  # the value of the parameter
        self.description = ""  # optional description of the parameter

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
