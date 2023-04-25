from logic import app_methods
from console_io import ConsoleIO

ACTIONS = {
    "x": "x quit",
    "1": "1 login",
    "2": "2 create item",
    "3": "3 create list",
    "4": "4 add item to list",
    "5": "5 delete list",
    "6": "6 logout",
    "7": "7 create new user"
}


class UserInterface:
    def __init__(self):
        self._io = ConsoleIO()
        self._methods = app_methods()

    def start(self):
        self._io.print("Grocery list app")
        self._print_instructions()

        while True:
            action = self._io.read("action: ")

            if not action in ACTIONS:
                self._io.print("nonexistent action")
                self._print_instructions()
                continue

            if action == "x":
                break
            elif action == "1":
                self._login()
            elif action == "2":
                self._create_item()
            elif action == "3":
                self._create_list()
            elif action == "4":
                self._add_item_to_list()
            elif action == "5":
                self._delete_list()
            elif action == "6":
                self._logout()
            elif action == "7":
                self._create_user()
        

    def _print_instructions(self):
        for value in ACTIONS.items():
            print(value)

    def _login(self):
        username = self._io.print("username: ")
        password = self._io.print("password: ")
        self._methods.login(username,password)

    def _create_user(self):
        self._io.print("creating new user:")
        username = self._io.read("username: ")
        password = self._io.read("username: ")
        self._methods.create_user(username,password)
        

    def _create_item(self):
        item_name = self._io.read("item name: ")

        self._methods.create_item(item_name)

    def _create_list(self):
        list_name = self._io.read("list name: ")

        self._methods.create_list(list_name)
        

    def _add_item_to_list(self):
        self._io.print("which item would you like to add:")

    def logout():



    # more todo