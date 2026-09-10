def my_discount() -> float:
    price: float = float(input("Enter the price: "))
    discount: float = float(input("Enter the discount percentage: "))

    discount_amount: float = price * discount / 100
    price_after_discount: float = price - discount_amount

    return price_after_discount



result: float = my_discount()

print("Price after discount:", result)