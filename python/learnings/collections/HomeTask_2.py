# Task 2

shedule = {
    '1001': ['пн', 'вс'],
    '1231': ['пн', 'вт'],
    '1232': ['ср', 'чт', 'пт'],
    '1280': ['ср', 'пт', 'вс'],
    '1282': ['чт'],
    '1290': ['пт', 'вс'],
    '1303': ['вт', 'вс'],
}

unique_days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']


def duty_days(shedule):
    values_list = [v for k, v in shedule.items()]
    days_list = [day for value in values_list for day in value]

    return days_list


def duty_staff(shedule, unique_days):
    k_list = []
    v_list = []

    for k, v in shedule.items():
        k_list.append(k)
        v_list.append(v)

    mon = [k_list[0] for days in v_list for day in days if unique_days[0] == day]
    tue = [k_list[1] for days in v_list for day in days if unique_days[1] == day]
    wed = [k_list[2] for days in v_list for day in days if unique_days[2] == day]
    thu = [k_list[3] for days in v_list for day in days if unique_days[3] == day]
    fri = [k_list[4] for days in v_list for day in days if unique_days[4] == day]
    sat = [k_list[5] for days in v_list for day in days if unique_days[5] == day]
    sun = [k_list[6] for days in v_list for day in days if unique_days[6] == day]

    staff = [len(mon), len(tue), len(wed), len(thu), len(fri), len(sat), len(sun)]

    return staff


def duty_on_days(shedule, unique_days):
    duty = {}
    staff = duty_staff(shedule, unique_days)

    for u, d in zip(unique_days, staff):
        duty[u] = d

    return duty


unduty_day = set(unique_days) ^ set(duty_days(shedule))
duty_dict = duty_on_days(shedule, unique_days)

print(f'Дни, когда никто не может дежурить: {unduty_day}')
print(f'Количество сотрудников по дням недели: {duty_dict}')
