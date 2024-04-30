import random

from src.utils import (get_vacancies_by_salary, filter_vacancies,
                       sort_vacancies,  get_top_vacancies, print_vacancies)


def test_print_vacancies(list_object_vacancies):
    assert print_vacancies(list_object_vacancies) is None


def test_get_top_vacancies(big_list_dict_vacancies, list_dict_vacancies_1,
                           list_dict_vacancies_2):
    assert (get_top_vacancies(big_list_dict_vacancies, 2)
            == big_list_dict_vacancies[:2])


def test_sort_vacancies(big_list_object_vacancies, list_dict_vacancies_1):
    random.shuffle(big_list_object_vacancies)
    assert sort_vacancies(big_list_object_vacancies)[0].__dict__ == \
           list_dict_vacancies_1[0]


def test_get_vacancies_by_salary(big_list_object_vacancies):
    assert get_vacancies_by_salary(big_list_object_vacancies,
                                   6000000)[-1].__dict__ == {
               "name": "Junior DevOps engineer",
               "salary_from": 6000000,
               "salary_to": None,
               "employer": "PROXIMAOPS",
               "currency": "узбек. сум",
               "experience": "От 1 года до 3 лет",
               "schedule": "Полный день",
               "employment": "Полная занятость",
               "requirement": "Знание git, CI \\ CD, Jenkins (написание скриптов сборок, дебаг, мониторинг). - Знание bash, <highlighttext>python</highlighttext> для написания скриптов и сценариев развертывания. - ",
               "responsibility": "Зона ответственности: - Обслуживание, мониторинг и поддержка инфраструктуры. - Совершенствование существующей инфраструктуры в целях повышения ее отказоустойчивости и масштабируемости. - Своевременное реагирование и...",
               "professional_roles": "Другое",
               "url": "https://hh.ru/vacancy/94442670"
           }


def test_filter_vacancies(big_list_object_vacancies):
    assert len(filter_vacancies(big_list_object_vacancies, ['backend', 'SQL'])) == 22
