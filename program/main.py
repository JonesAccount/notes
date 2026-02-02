from core import (
    ShowNote,
    AddNote,
    RemoveNote
)


class Main:
    _shownote = ShowNote()
    _addnote = AddNote()
    _removenote = RemoveNote()

    def menu(self):
        print("""       МЕНЮ
====================
1. Показать заметки
2. Добавить заметки
3. Удалить заметку
4. Удалить все заметки
5. Справка
6. Выход
====================
        """)
        self.start()


    def start(self):
        action = input("Действие: ")
        if action == "1":
            self._shownote.show_notes()
            main.menu()
        elif action == "2":
            self._addnote.add_note()
            main.menu()
        elif action == "3":
            self._removenote.remove_note()
            main.menu()


main = Main()
main.menu()