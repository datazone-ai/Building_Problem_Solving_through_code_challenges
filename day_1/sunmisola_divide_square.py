#Task

#Write a function called divide_or_square that takes one argument (a number):

#Returns the square root of the number if it is divisible by 5.
#Returns the remainder if it is not divisible by 5.
#Example: divide_or_square(10) → 3.16 (square root of 10)

import math
def divide_or_square(num):
    
    if num % 5 ==0 :
       return round(math.sqrt(num),2)
    else:
        return num % 5


    
