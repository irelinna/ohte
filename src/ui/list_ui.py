from tkinter import ttk, constants
from logic.app_methods import app_methods

class ListUI:

    def __init__(self,root,items):
        #konstruktori, luo näkymän listasta

        self._root = root
        self._items = items
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_item(self, item):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=item.content)

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        for item in self._items:
            self._initialize_item(item)

class ListView:

    def __init__(self, root, handle_logout):

        self._root = root
        self._handle_logout = handle_logout
        self._user = app_methods.get_user()
        self._frame = None

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_tool(self):
        app_methods.logout()
        self._handle_logout()

