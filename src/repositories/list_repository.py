from entities.list import List
from repositories.user_repository import user_repository
from pathlib import Path
from config import LISTS_FILE_PATH


class ListRepository:

    def __init__(self, file_path):
        self._file_path = file_path


    def find_all(self):
        return self._read()


    def find_by_username(self, username):
        lists = self.find_all()

        user_made_lists = filter(
            lambda list: list.user and list.user.username == username, lists)

        return list(user_made_lists)

    def create_list(self, list):
        #luo uuden listan tietokantaan
        lists = self.find_all()

        lists.append(list)

        self._write(lists)

        return list



    def delete(self, list_id):
        #poistaa tietyn listan
        #todo
        lists = self.find_all()

        lists_without_id = filter(lambda list: list.id != list_id, lists)

        self._write(lists_without_id)

    def delete_all(self):
        self._write([])

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        lists = []

        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                list_id = parts[0]
                content = parts[1]
                username = parts[2]

                user = user_repository.find_by_username(
                    username) if username else None

                lists.append(
                    List(content, user, list_id)
                )

        return lists

    def _write(self, lists):
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for list in lists:
                username = list.user.username if list.user else ""

                row = f"{list.id};{list.content};{username}"

                file.write(row+"\n")


list_repository = ListRepository(LISTS_FILE_PATH)