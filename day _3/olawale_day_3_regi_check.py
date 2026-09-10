def register_check(register: dict[str, str]) -> int:
    count: int = 0

    for student in register:
        if register[student] == "yes":
            count += 1

    return count


register = {
    "Michael": "yes",
    "John": "no",
    "Sarah": "yes",
    "David": "yes",
    "Peter": "no"
}

print(register_check(register))

    