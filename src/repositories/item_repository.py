from entities.item import Item
from repositories.user_repository import user_repository
from pathlib import Path
from config import ITEMS_FILE_PATH


class ItemRepository:

    def __init__(self, file_path):
        self._file_path = file_path


    def find_all(self):
        return self._read()


    def find_by_username(self, username):
        items = self.find_all()

        user_made_items = filter(
            lambda item: item.user and item.user.username == username, items)

        return list(user_made_items)

    def create_item(self, item):
        #luo tavaran tietokantaan
        items = self.find_all()

        items.append(item)

        self._write(items)

        return item



    def delete(self, item_id):
        #poistaa tietyn tavaran
        #todo
        items = self.find_all()

        items_without_id = filter(lambda item: item.id != item_id, items)

        self._write(items_without_id)

    def delete_all(self):
        self._write([])

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        items = []

        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                item_id = parts[0]
                content = parts[1]
                username = parts[2]

                user = user_repository.find_by_username(
                    username) if username else None

                items.append(
                    Item(content, user, item_id)
                )

        return items

    def _write(self, items):
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for item in items:
                username = item.user.username if item.user else ""

                row = f"{item.id};{item.content};{username}"

                file.write(row+"\n")


item_repository = ItemRepository(ITEMS_FILE_PATH)