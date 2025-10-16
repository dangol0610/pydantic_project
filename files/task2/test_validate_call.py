from pydantic import ValidationError

from files.task2.validate_call import add_numbers

def test_validate_call():
    try:
        add_numbers(1, 2)
        add_numbers("test", 123)
        print("Тест пройдены")
    except ValidationError as e:
        print("Ошибка валидации:", e)
    finally:
        print("Тест завершен")
