from logic import app_methods
from console_io import ConsoleIO

ACTIONS = {
    "x": "x quit",
    "1": "1 login",
    "2": "2 create new list",
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
        password = self._io.read("password: ")
        self._methods.create_user(username,password)

    def _create_item(self):
        self._methods.create_item(content, list_id)
        

    def _create_list(self):
        list_name = self._io.read("list name: ")

        self._methods.create_list(list_name)

        item_name = self._io.read("write the items you want to add one at a time, write exit to finish list:")

        while item_name != 'exit':
            self._methods.create_item(item_name)

        


    def _add_item_to_list(self):
        item = self._io.read("which item would you like to add?:")
        list = self._io.read("which list would you like to add it to?:")
        self._methods.add_item_to_list(item,list)

    def logout(self):
        self._methods.logout()


    # more todo