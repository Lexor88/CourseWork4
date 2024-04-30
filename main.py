import pathlib
from config import ROOT_DIR
from src.headhunterapi import HeadHunterAPI
from src.jsonworker import JSONWorker
from src.utils import (filter_vacancies, get_vacancies_by_salary,
                       sort_vacancies, get_top_vacancies, print_vacancies)
from src.vacancy import Vacancy


def main():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split(' ')
    salary_range = int(input("Введите нижний порог зарплаты: "))
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)
    file_name = input("Введите название файла, в который желаете произвести сохранение")
    file_path = pathlib.Path.joinpath(ROOT_DIR, 'data', file_name + '.json')
    json_saver = JSONWorker(file_path)
    json_saver.write_vacancies(top_vacancies)


if __name__ == "__main__":
    main()
