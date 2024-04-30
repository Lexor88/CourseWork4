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
