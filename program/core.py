from utils import border


class MotherClass:
    def func(self):
        try:
            with open('notes.txt', 'r') as file:
                lines = file.readlines()
                if len(lines) != 0:
                    border()
                    for line in range(len(lines)):
                        print(f"Заметка #{line + 1}: {lines[line]}", end="")
                    border()
                else:
                    print("Заметка пуста")
        except:
            print("Ошибка с файлами ❌")


class ShowNote(MotherClass):
    def show_notes(self):
        try:
            with open('notes.txt', 'r') as file:
                lines = file.readlines()
                if len(lines) != 0:
                    border()
                    for line in range(len(lines)):
                        print(f"Заметка #{line + 1}: {lines[line]}", end="")
                    border()
                else:
                    print("Заметка пуста")
        except:
            print("Ошибка с файлами ❌")


class AddNote:
    def add_note(self):
        try:
            with open('notes.txt', 'a') as file:
                new_note = input("Новая заметка: ")
                file.write(new_note + "\n")
        except:
            print("Ошибка с файлами ❌")


class RemoveNote:
    def remove_note(self):
        pass

