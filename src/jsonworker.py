import json

from src.fileworker import FileWorker


class JSONWorker(FileWorker):
    """
    Класс предназначенный для работы с файлами(имеет методы для выгрузки из файла, а так же
    для записи, добавления и удаления вакансий)
    """
    def __init__(self, path):
        self.path = path

    def load_vacancies(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            new_list = json.load(file)
            return new_list

    def write_vacancies(self, vacancies):
        with open(self.path, 'w', encoding='utf-8') as file:
            for_add = []
            for vacancy in vacancies:
                for_add.append(vacancy.__dict__)
            json.dump(for_add, file, ensure_ascii=False, indent=4)

    def add_vacancies(self, vacancies):
        with open(self.path, 'r', encoding='utf-8') as file:
            old_data = json.load(file)
            for vacancy in vacancies:
                old_data.append(vacancy.__dict__)
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(old_data, file, ensure_ascii=False, indent=4)

    def del_vacancy(self, vacancy):
        with open(self.path, 'r', encoding='utf-8') as file:
            old_data = json.load(file)
            if vacancy in old_data:
                old_data.remove(vacancy)
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(old_data, file, ensure_ascii=False, indent=4)
