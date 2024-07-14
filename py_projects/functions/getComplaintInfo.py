#  Данные о количестве жалоб на сбой в приложении такси за последние четыре недели
#  лежат в списке complaint_stat, где каждый элемент — это данные за все дни одной недели.
#  Вам нужно найти и вывести следующие значения для каждой недели:

#  Среднее количество жалоб (в случае дробного результата необходимо округлить до целого).
#  Количество дней, в которые количество жалоб было больше, чем их среднее количество.
#  Для решения данной задачи создайте три функции:

#  get_average_number — подсчёт среднего в списке;
#  outlier_days_count — подсчёт количества дней, в которые количество жалоб больше, чем среднее;
#  get_complaint_info — получение сводной информации (среднее количество жалоб и количество дней
#  с жалобами выше среднего) по списку.


complaint_stat = [
                  [27, 22, 15, 8, 3, 16, 15],
                  [12, 4, 10, 13, 29, 22, 121],
                  [5, 7, 6, 13, 2, 1, 25],
                  [15, 6, 14, 19, 25, 7, 3]
]


def get_average_number(week_stat):
    return round(sum(week_stat) / 7)  # делится на 7 (количество дней в неделе)


def outlier_days_count(week_stat, week_avg):
    outlier_days = 0
    for day in week_stat:
        if day > week_avg:
            outlier_days += 1
    return outlier_days


def get_complaint_info(complaint_stat):
    for week_stat in complaint_stat:
        week_avg = get_average_number(week_stat)
        outlier_days = outlier_days_count(week_stat, week_avg)
        print('Неделя ' + str(week_stat) + ': среднее = ' + str(week_avg) +
              ', количество дней, больших среднего: ' + str(outlier_days))


get_complaint_info(complaint_stat)