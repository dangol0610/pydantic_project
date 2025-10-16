from pydantic import validate_call

@validate_call
def add_numbers(arg1: int, arg2: int) -> int:
    return arg1 + arg2