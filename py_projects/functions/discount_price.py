def discount_price(items_price, discount):

    if items_price == []:
        return None

    total_price = sum(items_price)
    total_discount = total_price - discount / 100 * total_price

    return total_price, total_discount

print(discount_price([1, 12, 10, 99], 10))
