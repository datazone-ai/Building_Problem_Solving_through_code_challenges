FUNCTION my_discount() -> Float

    INPUT:
        price: Float
        discount: Float

    OUTPUT:
        price_after_discount: Float

    BEGIN

        ASK user to enter the price
        STORE the input as price

        ASK user to enter the discount percentage
        STORE the input as discount

        CALCULATE discount_amount
            discount_amount = price × discount ÷ 100

        CALCULATE price_after_discount
            price_after_discount = price - discount_amount

        RETURN price_after_discount

    END FUNCTION