FUNCTION string_range(number)
    CREATE an empty list

    FOR each number from 0 up to number - 1
        CONVERT the number to a string
        ADD the string to the list
    END FOR

    JOIN all the strings using "."
    RETURN the resulting string
END FUNCTION