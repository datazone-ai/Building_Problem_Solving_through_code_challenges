from typing import Any

def only_floats(a: Any, b: Any) -> int:
    count: int = 0

    if isinstance(a, float):
        count += 1

    if isinstance(b, float):
        count += 1

    return count

print(only_floats(2.5, 4.7))  
print(only_floats(2.5, 4))    
print(only_floats(2, 4))      