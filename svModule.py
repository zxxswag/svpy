from svPort import svPort  # Importing the Port class from Port.py
from svParameter import svParameter  # Importing the Parameter class from Parameter.py


class svModule:
    def __init__(self, identifier: str):
        self.identifier: str = identifier  # the identifier of the module
        self.port_list = []  # list of ports in the module
        self.parameter_list = []  # list of parameters in the module
        self.package_list = []  # list of packages in the module
        self.module_header_style = (
            "ANSI"  # the style of the module header, other is 'non-ANSI'
        )
        self.lifetime = "static"  # the lifetime of the module, other is 'automatic'

    def set_identifier(self, identifier: str):
        self.identifier = identifier

    def get_identifier(self) -> str:
        return self.identifier

    def set_module_header_style(self, style: str):
        if style not in ["ANSI", "non-ANSI"]:
            raise ValueError(
                "Invalid module header style. Choose 'ANSI' or 'non-ANSI'."
            )
        self.module_header_style = style

    def set_lifetime(self, lifetime: str):
        if lifetime not in ["static", "automatic"]:
            raise ValueError("Invalid lifetime. Choose 'static' or 'automatic'.")
        self.lifetime = lifetime

    def add_port(self, port):
        if (
            not hasattr(port, "name")
            or not hasattr(port, "direction")
            or not hasattr(port, "size")
        ):
            raise ValueError(
                "Port must have 'name', 'direction', and 'size' attributes."
            )
        self.port_list.append(port)

    def remove_port(self, port):
        if port not in self.port_list:
            raise ValueError("Port not found in the module.")
        self.port_list.remove(port)

    def add_parameter(self, parameter):
        if (
            not hasattr(parameter, "name")
            or not hasattr(parameter, "value")
            or not hasattr(parameter, "description")
        ):
            raise ValueError(
                "Parameter must have 'name', 'value', and 'description' attributes."
            )
        self.parameter_list.append(parameter)

    def get_port_in(self):
        return [port for port in self.port_list if port.get_direction() == "input"]

    def get_port_out(self):
        return [port for port in self.port_list if port.get_direction() == "output"]

    def get_port_inout(self):
        return [port for port in self.port_list if port.get_direction() == "inout"]

    def create_code(self):
        lines = []
        if self.module_header_style == "non-ANSI":
            lines.append(
                f"module {'' if self.lifetime == 'static' else 'automatic '}{self.identifier} ("
            )
            if self.port_list:
                lines.append("\t// port_list")
                lines.append(
                    "\n".join(
                        [
                            "\t"
                            + port.get_name()
                            + ("," if idx < len(self.port_list) - 1 else "")
                            + (
                                f" // {port.get_description()}"
                                if port.get_description() != ""
                                else ""
                            )
                            for idx, port in enumerate(self.port_list)
                        ]
                    )
                )
            lines.append(");")
            if self.parameter_list:
                lines.append("\t// parameter_declaration_list")
                lines.append(
                    "\n".join(
                        [
                            "\tparameter "
                            + parameter.get_name()
                            + " = "
                            + str(parameter.get_value())
                            + ";"
                            for parameter in self.parameter_list
                        ]
                    )
                )
            if self.port_list:
                lines.append("\t// port_direction_and_size_declarations")
                lines.append(
                    "\n".join(
                        f"\t{port.get_direction()} {'[' + str(port.get_size()-1) + ':0] ' if port.get_size() != 1 else ''}{port.get_name()};"
                        for port in self.port_list
                    )
                )
                lines.append("\t// port_type_declarations")
                lines.append(
                    "\n".join(
                        [
                            f"\t{port.get_datatype()} {port.get_name()};"
                            for port in self.port_list
                        ]
                    )
                )
            lines.append(f"endmodule : {self.identifier}")
        else:
            lines.append(
                f"module {'' if self.lifetime == 'static' else 'automatic '}{self.identifier} {'#(' if self.parameter_list else '('}"
            )
            if self.parameter_list:
                lines.append(
                    "\n".join(
                        [
                            "\t"
                            + "parameter "
                            + parameter.get_name()
                            + " = "
                            + str(parameter.get_value())
                            + ("," if idx < len(self.parameter_list) - 1 else "")
                            + (
                                f" // {parameter.get_description()}"
                                if parameter.get_description() != ""
                                else ""
                            )
                            for idx, parameter in enumerate(self.parameter_list)
                        ]
                    )
                )
                lines.append(") (")
            lines.append(
                "\n".join(
                    [
                        "\t"
                        + port.get_direction()
                        + " "
                        + port.get_datatype()
                        + " "
                        + ("signed " if port.get_signedness() != "unsigned" else "")
                        + (
                            "[" + str(port.get_size() - 1) + ":0] "
                            if port.get_size() != 1
                            else ""
                        )
                        + port.get_name()
                        + ("," if idx < len(self.port_list) - 1 else "")
                        + (
                            f" // {port.get_description()}"
                            if port.get_description() != ""
                            else ""
                        )
                        for idx, port in enumerate(self.port_list)
                    ]
                )
            )
            lines.append(f");")
            lines.append(f"endmodule : {self.identifier}")
        with open(f"{self.identifier}.sv", "w", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")


if __name__ == "__main__":
    module = svModule("ExampleModule")
    module.add_port(svPort("clk", 2, "input", description="Clock signal"))
    module.add_port(svPort("rst", 1, "input", description="Reset signal"))
    module.set_module_header_style("ANSI")
    module.add_parameter(svParameter("WIDTH", 8, description="Width of the data bus"))
    module.add_parameter(svParameter("ADDR", 8, description="Width of the address bus"))
    module.create_code()
