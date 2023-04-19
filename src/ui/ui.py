from ui.login_ui import LoginUI
from ui.create_new_user_ui import CreateNewUserUI
from ui.list_ui import ListUI

class UI:
   #sovelluksen käyttöliittymä

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        #käynnistys
        self._show_login_view()

    def _hide_current_view(self):
        #piilota näkymä
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        #näytä login-sivu
        self._hide_current_view()

        self._current_view = LoginUI(
            self._root,
            self._show_todos_view,
            self._show_create_user_view
        )

        self._current_view.pack()

    def _show_list_view(self):
        self._hide_current_view()

        self._current_view = ListUI(self._root, self._show_login_view)

        self._current_view.pack()


    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateNewUserUI(
            self._root,
            self._show_todos_view,
            self._show_login_view
        )

        self._current_view.pack()