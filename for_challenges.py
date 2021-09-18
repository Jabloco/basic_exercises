# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']

def print_name(input_names: list):
    for name in input_names:
        print(name)

print_name(names)

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']

def name_and_length(input_names: list):
    for name in input_names:
        print(f'{name}: {len(name)}')

name_and_length(names)

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Женя', 'Вася', 'Маша']

def name_and_gender(input_names: list, input_gender: dict):
    for name in input_names:
        get_gender = input_gender.get(name)
        try:
            if get_gender is None:
                raise KeyError('Пол не известен')
        except KeyError as error:
            print(f"{name} {error}")
            continue

        if get_gender:
            male_or_famale = "М"
        else:
            male_or_famale = "Ж"
        
        print(f"{name} {male_or_famale}")

name_and_gender(names, is_male)
# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]

def group_info(input_groups: list):
    print(f'Всего групп: {len(input_groups)}')
    group_count = 0
    for group in input_groups:
        group_count += 1
        print(f'Группа {group_count}: {len(group)} ученика')
        
group_info(groups)

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]

def group_content(input_group: list):
    group_count = 0
    for group in input_group:
        group_count += 1
        person_in_group = ", ".join(group)
        print(f'Группа {group_count}: {person_in_group}')

group_content(groups)