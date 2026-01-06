class InputReader:
    def integer(self, label: str = "Ingrese un número entero") -> int:
        """Reads an string and converts it to an integer."""
        try:
            value = input(f"{label}: ")
            return int(value)
        except ValueError:
            print("Entrada inválida, ingrese un número entero válido.")
            return self.integer(label)

    def float(self, label: str = "Ingrese un número decimal") -> float:
        """Reads a string and converts it to a float."""
        try:
            value = input(f"{label}: ")
            return float(value)
        except ValueError:
            print("Entrada inválida, ingrese un número decimal válido.")
            return self.float(label)

    def string(
        self, label: str = "Ingrese una cadena de texto", empty: bool = False
    ) -> str:
        """Reads a string from standard input."""
        value = input(f"{label}: ")
        if not empty and not value:
            print("La entrada no puede estar vacía.")
            return self.string(label, empty)
        return value

    def character(self, label: str = "Ingrese un carácter", upper: bool = False) -> str:
        """Reads a non-empty string from standard input and returns the first character in uppercase if upper is True, lowercase if False."""
        value = input(f"{label}: ")
        if not value:
            print("La entrada no puede estar vacía.")
            return self.character(label, upper)
        if upper:
            value = value.upper()
        return value[0]
