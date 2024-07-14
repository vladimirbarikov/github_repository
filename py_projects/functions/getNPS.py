# индекс NPS - Net Promoter Score
# (англ. — индекс потребительской лояльности) - это показатель
# приверженности потребителей товару или компании.
# Замеры построены на вопросе, рекомендует ли клиент компанию своим друзьям,
# с оценкой от 0 до 10 баллов.

def nps(scores):
    positive_count = 0
    negative_count = 0
    for score in scores:
        if score >= 9:
            positive_count += 1
        elif score <= 6:
            negative_count += 1
    nps = (positive_count - negative_count) / len(scores)
    nps = nps * 100
    return nps


def extend_list(scores_list):
    scores = []
    for elem in scores_list:
        scores.extend(elem)
    return scores


def total_nps(scores_list):
    result_list = extend_list(scores_list)
    return nps(result_list)


scores_list = [
    [10, 10, 9, 10, 1, 8, 5],
    [9, 9, 8, 5],
    [10, 10, 10, 4, 5]
]

for scores in scores_list:
    print(nps(scores))
print(total_nps(scores_list))
