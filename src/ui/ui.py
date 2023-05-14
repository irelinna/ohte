from logic.app_methods import app_methods

ACTIONS = {
    "0": "0 quit",
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
        self._methods = app_methods
    

    def start(self):
        """Starts the application and shows the UI to the user.
        """

        print("Grocery list app\n")
        self._print_instructions()

        while True:
            action = input("action: ")
            if not action in ACTIONS:
                print("nonexistent action\n")
                self._print_instructions()
                continue
            elif action == "" or action == None:
                print("empty input is not valid\n")
                self._print_instructions()
            elif action == "0":
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
        user = self._methods.get_user()
        if user:
            print("current user is: ", user.username)

        for value in ACTIONS.items():
            print(value[1])
        print("\n")


    def _login(self):
        """Reads input for login.
        """
        if self._methods.get_user() == None:
            username = input("username: ")
            password = input("password: ")
            if self._methods.login(username,password) == False:
                print("Invalid username or password\n")
            else:
                print("Logged in successfully!\n")
        else:
            print("You seem to be logged in already. Log out first.\n")


        self._print_instructions()


    def _create_user(self):
        """UI for creating a new user.
        """
        if self._methods.get_user() == None:
            print("creating new user:\n")
            username = input("username: ")
            password = input("password: ")
            print("\n")
            self._methods.create_user(username,password)
            self._print_instructions()
        else:
            action = input("You seem to be logged in. Do you want to log out? (y/n)\n")
            if action == "y":
                self._logout()
            elif action == "n":
                self._print_instructions()
            else:
                print("invalid action")
                self._print_instructions()
        

    def _create_list(self):
        """UI for creating a new list.
        """
        if self._methods.get_user() == None:
            print("you must be logged in to create a list.\n")
        else:
            username = self._methods.get_user().username
            print("creating list")
            list_name = input("list name:\n")
            self._methods.create_list(list_name, username)

            list_id = self._methods.get_list_id(list_name)

            print("write the items you want to add one at a time, write exit to finish list:")
            item_name = "item"
            while item_name != 'exit':
                if item_name == "" or item_name == " ":
                    print("empty items cannot be added")
                item_name = input("item: ")
                if item_name == 'exit':
                    print("\n")
                    break

                self._methods.create_item(list_id,item_name)

        
        self._print_instructions()

    def _find_list(self):
        """Finds a list by list name and prints out items from that list.
        """
        list_name = input("which list would you like to see:\n")

        items = self._methods.find_list_by_name(list_name)

        print("Here are the items from list", list_name, ":")
        for item in items:
            print(item)
        print("\n")
        
        self._print_instructions()


    def _delete_list(self):
        """Deletes a list.
        """
        list_name = input("which list would you like removed:\n")
        self._methods.delete_list(list_name)
        print("list removed successfully.\n")
        self._print_instructions()


    def _add_item_to_list(self):
        """UI for adding an item to an existing list."""

        item = input("which item would you like to add?:\n")
        list = input("which list would you like to add it to?:\n")

        self._methods.add_item_to_list(item,list)
        print("item added to list.\n")
        self._print_instructions()

    def _logout(self):
        """Method for logging out.
        """
        if self._methods.get_user() == None:
            print("You don't seem to be logged in.\n")
        else:
            self._methods.logout()
            if self._methods.get_user() == None:
                print("Logged out successfully!\n")
        self._print_instructions()
