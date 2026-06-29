from typing import Optional, Any,List,Union

def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name("John"))


def process_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"

print(process_value(1))


def process_anything(value: Any) -> str:
    return f"Processed {value}"
print(process_anything("Digital School"))


def sum_list(numbers: List[int]) -> int:
    return sum(numbers)

print(sum_list([1, 2, 3]))




