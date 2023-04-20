import json


def load_students(path):
    """
    Загружает список студентов из файла
    """
    with open(path, 'r', encoding="utf-8") as file:
        student = json.load(file)
        return student


def load_professions(path):
    """
    Загружает список профессий из файла
    """
    with open(path, encoding="utf-8") as file:
        profession = json.load(file)
        return profession


def get_student_by_pk(all_students, pk):
    """
    Получает словарь с данными студента по его pk
    """
    for stud in all_students:
        if stud["pk"] == pk:
            return stud


def get_profession_by_title(all_professions, title):
    """
    Получает словарь с инфо о профессии по названию
    """
    for pro in all_professions:
        if pro["title"].lower() == title.lower():
            return pro


def check_fitness(student, profession):
    """
    Получив студента и профессию, возвращает словарь
    """
    stud_skillset = set(student)
    pro_skillset = set(profession)

    has = stud_skillset.intersection(pro_skillset)
    lacks = pro_skillset.difference(stud_skillset)
    fit_percent = len(has) / len(pro_skillset)

    return {
        "has": has,
        "lacks": lacks,
        "fit_percent": round(fit_percent * 100)
    }
