class svPackage:
    def __init__(self, identifier):
        self.identifier: str = identifier
        self.lifetime = "static"  # Default lifetime, other is 'automatic'

    def set_identifier(self, identifier):
        self.identifier = identifier

    def get_identifier(self):
        return self.identifier

    def set_lifetime(self, lifetime):
        self.lifetime = lifetime

    def get_lifetime(self):
        return self.lifetime
