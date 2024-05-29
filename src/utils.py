from src.company import Company
from src.dbmanager import DBManager
from src.headhunterapi import HeadHunterAPI
from src.vacancy import Vacancy


def filter_vacancies(vacancies_list, words_for_filter):
    """
    :param vacancies_list: принимаемый лист для фильтрации по словам
    :param words_for_filter: список слов, принимаемый для фильтрации списка
    :return: отфильтрованный список
    """
    filtered_list = []
    for vacancy in vacancies_list:
        for word in words_for_filter:
            if word in vacancy.responsibility or word in vacancy.requirement:
                filtered_list.append(vacancy)
                break
    return filtered_list


def get_vacancies_by_salary(vacancies, min_salary):
    """
    :param vacancies: список вакансий из которого вернутся лишь те зарплаты, чьё
    значение выше поступившего аргумента min_salary
    :param min_salary: значение зарплаты служащее фильтром для списка вакансий
    :return: список вакансий с зарплатами выше указанной
    """
    only_salary_vacancies = []
    for vacancy in vacancies:
        if vacancy >= min_salary:
            only_salary_vacancies.append(vacancy)
    return only_salary_vacancies


def sort_vacancies(vacancies):
    """Возвращает списко вакансий, отсортированный по минимальной заработной
    плате"""
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies, stop):
    """Возвращает срез от списка vacancies"""
    return vacancies[:stop]


def print_vacancies(vacancies):
    """Печатает каждую вакансию из поданного списка"""
    for vacancy in vacancies:
        print(vacancy)


def add_data_to_db():
    db = DBManager()
    company_ids = ['3127', '3776', '1122462', '2180', '87021',
                   '1740', '80', '4181', '15478', '78638']
    hh_api = HeadHunterAPI()
    hh_vacancies = []
    for company_id in company_ids:
        hh_vacancies = hh_api.load_vacancies(employer_id=company_id)
    hh_companies = hh_api.load_companies(company_ids)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    companies_list = Company.get_list_with_objects(hh_companies)
    db.load_to_db(vacancies_list, companies_list)
    db.conn.close()
    print('Таблицы были заполнены/перезаполнены')
