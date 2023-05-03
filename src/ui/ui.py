from logic.app_methods import AppMethods

ACTIONS = {
    "x": "x quit",
    "1": "1 login",
    "2": "2 create new user",
    "3": "3 create new list",
    "4": "4 add item to list",
    "5": "5 find list",
    "6": "6 delete list",
    "7": "7 logout"
}


class UserInterface:
    """Class responsible for the user interface.
    """
    def __init__(self):
        """Constructor
        """
        self._methods = AppMethods()
    

    def start(self):
        """Starts the application and shows the UI to the user.
        """

        print("Grocery list app")
        self._print_instructions()

        while True:
            action = input("action: ")

            if not action in ACTIONS:
                print("nonexistent action")
                self._print_instructions()
                continue

            if action == "x":
                break
            elif action == "1":
                self._login()
            elif action == "2":
                self._create_user()
            elif action == "3":
                self._create_list()
            elif action == "4":
                self._add_item_to_list()
            elif action == "5":
                self._find_list()
            elif action == "6":
                self._delete_list()
            elif action == "7":
                self._logout()  
        

    def _print_instructions(self):
        """Prints instructions from dictionary ACTIONS.
        """

        for value in ACTIONS.items():
            print(value)


    def _login(self):
        """Reads input for login.
        """
        username = print("username: ")
        password = print("password: ")
        self._methods.login(username,password)


    def _create_user(self):
        if self._methods.get_user() == None:
            print("creating new user:")
            username = input("username: ")
            password = input("password: ")
            self._methods.create_user(username,password)
        else:
            action = input("You seem to be logged in. Do you want to log out? y/n")
            if action == "y":
                self._logout()
            elif action == "n":
                self._print_instructions()
            else:
                print("invalid action")
                self._print_instructions()

    def _create_item(self, content, list_id):
        self._methods.create_item(content, list_id)
        

    def _create_list(self):
        list_name = input("list name: ")
        self._methods.create_list(list_name)

        list_id = self._methods.get_list_id(list_name)

        item_name = input("write the items you want to add one at a time, write exit to finish list:")

        while item_name != 'exit':
            self._methods.create_item(item_name, list_id)

    def _find_list(self):
        list_name = input("which list would you like to see:")

        self._methods.find_list_by_name(list_name)


    def _delete_list(self):
        list_name = input("which list would you like removed: ")
        self._methods.delete_list(list_name)


    def _add_item_to_list(self):
        item = input("which item would you like to add?:")
        list = input("which list would you like to add it to?:")
        self._methods.add_item_to_list(item,list)

    def _logout(self):
        self._methods.logout()
