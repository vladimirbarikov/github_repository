dates = ['1999-10-01', '2001-12-17', '1991-12-01', '2001-01-01', '2001-06-22', '2001-09-05', '2001-01-13']


def dates_to_tuples(dates):
    converted_dates = []
    for date in dates:
        tuple_date = date.split('-')
        tuple_date = (int(tuple_date[0]), int(tuple_date[1]), int(tuple_date[2]))
        converted_dates.append(tuple_date)

    return converted_dates


tuple_dates = dates_to_tuples(dates)

print((1990, 10, 1) in tuple_dates)

print((1999, 10, 1) in tuple_dates)
