START

FUNCTION odd_even(numbers)

    CREATE an empty list called even_numbers
    CREATE an empty list called odd_numbers

    FOR each number in numbers
        IF number is divisible by 2
            ADD number to even_numbers
        ELSE
            ADD number to odd_numbers
        END IF
    END FOR

    FIND the largest number in even_numbers
    FIND the smallest number in odd_numbers

    SUBTRACT the smallest odd number from the largest even number

    RETURN the result

END FUNCTION

END