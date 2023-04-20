import os.path

from utils import load_professions, load_students, check_fitness, get_profession_by_title, get_student_by_pk

STUDENT_PATH = os.path.join("students.json")
PROFESSION_PATH = os.path.join("professions.json")


def main():
    all_students = load_students(STUDENT_PATH)
    all_profession = load_professions(PROFESSION_PATH)

    print("Введите номер студента")
    student_pk = int(input())
    student = get_student_by_pk(all_students, student_pk)

    if student is None:
        print("Такого студента нет")
        return

    stu_name, stu_skills = student["full_name"], ", ".join(student["skills"])

    print(f"Студент {stu_name}")
    print(f"Знает {stu_skills}")

    print(f"Выберите специальность для оценки студента")
    request_proffession = input()
    profession = get_profession_by_title(all_profession, request_proffession)

    if profession is None:
        print("Такой профессии нет")
        return

    stud_skills = student["skills"]
    pro_skills = profession["skills"]

    fitness_dikt = check_fitness(stud_skills, pro_skills)

    has = ", ".join(fitness_dikt["has"])
    fit_percent = fitness_dikt["fit_percent"]
    lacks = ", ".join(fitness_dikt["lacks"])

    print(f'Пригодность {fit_percent}%')
    print(f'{stu_name} знает {has}')
    print(f'{stu_name} не знает {lacks}')


main()
