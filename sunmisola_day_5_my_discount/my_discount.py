def my_discount():
    price = (float("Enter the price: "))
    discount = (float("Enter the discount(%): "))

    discount_amount = price * discount/100
    final_price = price - discount_amount

    return final_price

