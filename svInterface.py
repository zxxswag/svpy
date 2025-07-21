class svInterface(object):

    def __init__(self, identifier):
        self.identifier: str = identifier
        self.parameter_list = []  # list of parameters in the interface

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, identifier):
        self.identifier = identifier
