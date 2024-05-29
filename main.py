import pathlib
from config import ROOT_DIR
from src.dbmanager import DBManager
from src.headhunterapi import HeadHunterAPI
from src.jsonworker import JSONWorker
from src.utils import (filter_vacancies, get_vacancies_by_salary,
                       sort_vacancies, get_top_vacancies, print_vacancies, add_data_to_db)
from src.vacancy import Vacancy


def main():
    user_input = input("Желаете обновить базу данных? yes/no")
    if user_input == 'yes':
        add_data_to_db()
    user_input = input("Какой запрос желаете направить в БД\n"
                       "1 - получить список всех компаний и количество вакансий у каждой компании\n"
                       "2 - получить список всех вакансий с указанием названия компании, названия "
                       "вакансии и зарплаты и ссылки на вакансию\n"
                       "3 - получить среднюю зарплату по вакансиям\n"
                       "4 - получить список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
                       "5 - получить список всех вакансий, в названии которых содержатся переданные в метод слова, "
                       "например python.\n")
    dbmanager = DBManager()
    if user_input == '1':
        for i in dbmanager.get_companies_and_vacancies_count():
            print(i)
    elif user_input == '2':
        for i in dbmanager.get_all_vacancies():
            print(i)
    elif user_input == '3':
            print(dbmanager.get_avg_salary())
    elif user_input == '4':
        for i in dbmanager.get_vacancies_with_higher_salary():
            print(i)
    elif user_input == '5':
        search_query = input("Введите поисковый запрос: ")
        for i in dbmanager.get_vacancies_with_keyword(search_query):
            print(i)
    else:
        print('Команда не была распознана')


if __name__ == "__main__":
    main()
