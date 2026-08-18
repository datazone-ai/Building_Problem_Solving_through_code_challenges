
import math
from typing import Union
def divide_or_square(number: int | float)-> int | float: 
    
    if number % 5 == 0:
        return round(math.sqrt(number), 2)
    else:
        return number % 5
    
assert divide_or_square(10) == 3.16
assert divide_or_square(8) == 3