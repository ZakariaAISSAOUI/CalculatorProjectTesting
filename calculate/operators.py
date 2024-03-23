class Operators:
    def __init__(self):
        self.operation = ""
        self.operator = ""
        self.result = 0.0

    def addition(self, operation):
        """
            Handles an addition operation.

            :param operation: The requested operation by user.
            :return: The addition result if the operation is valid.
        """
        self.operation = operation
        self.operator = "+"
        if self._is_operation_valid():
            self._calculate_addition()
            return self.result

    def subtraction(self, operation):
        """
            Handles a subtraction operation.

            :param operation: The requested operation by user.
            :return: The subtraction result if the operation is valid.
        """
        self.operation = operation
        self.operator = "-"
        if self._is_operation_valid():
            self._calculate_subtraction()
            return self.result

    def multiplication(self, operation):
        """
            Handles a multiplication operation.

            :param operation: The requested operation by user.
            :return: The multiplication result if the operation is valid.
        """
        self.operation = operation
        self.operator = "*"
        if self._is_operation_valid():
            self._calculate_multiplication()
            return self.result

    def division(self, operation):
        """
            Handles a division operation.

            :param operation: The requested operation by user.
            :return: The division result if the operation is valid.
        """
        self.operation = operation
        self.operator = "/"
        if self._is_operation_valid():
            self._calculate_division()
            return self.result

    def _is_operation_valid(self):
        """
            Checks if the operation have the correct syntax.

            :return: True if the operation is valid
        """
        if self._is_symbol_valid():
            self.numbers = self.operation.split(self.operator[0])
            for number in self.numbers:
                if not self._is_float(number):
                    return False
            return True
        return False

    def _is_symbol_valid(self):
        """
            Checks if the operation matches with the type of operation requested by the user.

            :return: True if all symbols in the operation are valid.
        """
        symbols = [symbol for symbol in self.operation if not symbol.isdigit()]
        for symbol in symbols:
            if symbol != self.operator and symbol != "." and symbol != " ":
                return False
        return True

    def _is_float(self, value):
        """
            Checks if the given symbol can be converted to float value.

            :return: True if the symbol can be converted to float value.
        """
        try:
            float(value)
            return True
        except ValueError:
            return False

    def _calculate_addition(self):
        """
            Makes the addition calculation.
        """
        self.result = 0.0
        for number in self.numbers:
            self.result += float(number)

    def _calculate_subtraction(self):
        """
            Makes the subtraction calculation.
        """
        self.result = float(self.numbers[0])
        for i in range(1, len(self.numbers)):
            self.result -= float(self.numbers[i])

    def _calculate_multiplication(self):
        """
            Makes the multiplication calculation.
        """
        self.result = 1.0
        for number in self.numbers:
            self.result *= float(number)

    def _calculate_division(self):
        """
            Makes the division calculation.
        """
        self.result = float(self.numbers[0])
        for i in range(1, len(self.numbers)):
            try:
                self.result /= float(self.numbers[i])
            except ZeroDivisionError:
                self.result = None
