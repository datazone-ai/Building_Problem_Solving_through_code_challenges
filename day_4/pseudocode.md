FUNCTION 
only_floats(a: Any, b: Any) -> Integer

INPUT:
    a: Any data type
    b: Any data type

OUTPUT:
    Integer:
        2 if both a and b are floats
        1 if only one of a or b is a float
         0 if neither a nor b is a float

    SET count: Integer = 0

    IF a is a Float THEN
        count = count + 1
    

    IF b is a Float THEN
        count = count + 1
    

    RETURN count

END FUNCTION