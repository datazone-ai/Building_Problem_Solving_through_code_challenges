FUNCTION 
register_check(register: Dictionary<String, String>) -> Integer

    INPUT:
        register: Dictionary<String, String>
        - Key: student name (String)
        - Value: attendance status (String)
        - Status can be "yes" or "no"

    OUTPUT:
        Integer
        - The number of students who are in school

    SET count: Integer = 0

    FOR each student: String in register

        IF register[student] == "yes" THEN
            count = count + 1
        

    RETURN count

END FUNCTION