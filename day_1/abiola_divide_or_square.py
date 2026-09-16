"""
    Task

Write a function called divide_or_square that takes one argument (a number):

Returns the square root of the number if it is divisible by 5.
Returns the remainder if it is not divisible by 5.

Example: divide_or_square(10) → 3.16 (square root of 10)
""""


def divide_or_square(number: int | float) -> int | float:
    if number % 5 == 0 :
        return  round(number ** 0.5, 2)
    else:
        return number % 5



# approach
import math
from typing import Union

def divide_or_square(number: Union[int, float]) -> Union[int, float]:
    if number % 5:
        return round(math.sqrt(number), 2)
    else:
        return number % 5


assert divide_or_square(10) = 3.16
