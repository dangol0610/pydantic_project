from files.task3.schemas import Deal
from settings.settings import settings


class DealsDescriptor:
    def __get__(self, instance, owner):
        return instance._deals

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError("Должен быть список сделок")
        if not all(isinstance(item, Deal) for item in value):
            raise ValueError("Все элементы должны быть экземплярами Deal")
        instance._deals = value

    def __delete__(self, instance):
        instance._deals = []


class DealsStore:
    _instance = None
    deals = DealsDescriptor()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self._deals = []

    def get_store(self):
        return self.deals

    def set_store_data(self, deals: list[Deal]):
        self.deals = deals


class ConnectionStore:
    def __enter__(self):
        print(f"Подключение к хранилищу по адресу: {settings.db_url}")
        return DealsStore()
    
    def __exit__(self, exc_type, exc_val, traceback):
        print(f"Отключение от хранилища по адресу: {settings.db_url}")