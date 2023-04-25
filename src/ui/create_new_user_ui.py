from tkinter import ttk, StringVar, constants
from logic.app_methods import app_methods, UsernameExistsError


class CreateNewUserUI:

    def __init__(self, root, handle_create_user, handle_show_login_view):
        #luo uuden rekisteröitymisnäkymän
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        #näyttää sivun
        self._frame.pack(fill=constants.X)

    def destroy(self):
        #tuhoaa sivun
        self._frame.destroy()

    def _create_user_handler(self):
        #hoitaa uuden käyttäjän luomisen
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Username or password field empty")
            return

        try:
            app_methods.create_user(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f"Username {username} already exists")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="orange"
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        create_user_button = ttk.Button(
            master=self._frame,
            text="Create new user",
            command=self._create_user_handler
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._handle_show_login_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()