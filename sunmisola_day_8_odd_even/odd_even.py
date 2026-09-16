def odd_even(nums):
    odd_num = []
    even_num = []

    for number in nums:
       if number % 2 ==0:  
          even_num.append(number)
    else:
       odd_num.append(number)

       largest_even =max(even_num)
       smallest_odd =min(odd_num)

    return largest_even - smallest_odd
           
       
    