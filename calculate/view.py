class View:
    @staticmethod
    def print_menu():
        """
            Prints all menu items and the corresponding number.
        """
        print("\n=========== MENU ===========")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Exit")
        print("============================\n")

    @staticmethod
    def get_user_input(input_message):
        """
            Function to ask an input.

            :param input_message: Message insert into the input function.
            :return: The user input.
        """
        user_input = input(f"{input_message} : ")
        return user_input

    @staticmethod
    def end_message():
        """
            Prints the end message at the end of the script.
        """
        print("=========== GOOD-BYE ===========")

    @staticmethod
    def continue_message():
        """
            Requests to press enter to continue.
        """
        input("Press ENTER to continue ...")

    @staticmethod
    def print_result(operation, result):
        """
            Prints the result if the operation is valid otherwise print an error message.

            :param operation: The operation request by the user
            :param result: The result calculate by the script
        """
        if result is not None:
            print(f"RESULT : {operation} = {result}")
        else:
            print(f"Your operation is wrong! : {operation}")
