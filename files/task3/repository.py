from files.task3.schemas import Deal, User
from files.task3.store import ConnectionStore, DealsStore


class DealsRepository:
    def __init__(self, model: DealsStore, connection: ConnectionStore):
            self._model = model
            self._connection = connection
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        if hasattr(self, '_model'):
            raise AttributeError("Нельзя заменить уже установленную модель")
        self._model = value
    
    @model.deleter
    def model(self):
        del self._model

    def create_deal(self, deals: list[Deal] | Deal):
        with self._connection as store:
            store_data = store.get_store()
            errors = []
            for deal in deals if isinstance(deals, list) else [deals]:
                try:
                    if not isinstance(deal, Deal):
                        errors.append((deal, TypeError(f"Ожидался объект Deal, получен {type(deal)}")))
                        continue
                    store_data.append(deal)
                except Exception as e:
                    errors.append((deal, e))
            store.set_store_data(store_data)
            if errors:
                for deal, error in errors:
                    print(f"Ошибка при добавлении сделки {deal}: {error}")  

    def get_deals(self) -> list[Deal]:
        with self._connection as store:
            return store.get_store()
    
    def get_deals_dict(self) -> list[dict]:
        with self._connection as store:
            return [deal.model_dump() for deal in store.get_store()]
        
    def get_deal(self, id) -> Deal:
        with self._connection as store:
            for deal in store.get_store():
                if deal.id == id:
                    return deal
            raise ValueError(f"Сделка с id: {id} не найдена")
    
    def delete_deal(self, id):
        with self._connection as store:
            store_data = store.get_store()
            for i, deal in enumerate(store_data):
                if deal.id == id:
                    store_data.pop(i)
                    store.set_store_data(store_data)
                    return
            raise ValueError(f"Сделка с id: {id} не найдена")
        
    def update_deal(self, id, value: Deal | User):
        with self._connection as store:
            store_data = store.get_store()
            for i, deal in enumerate(store_data):
                if deal.id == id:
                    if isinstance(value, Deal):
                        store_data[i] = value
                    elif isinstance(value, User):
                        deal.persons_in_charge.append(value)
                    else:
                        raise ValueError("Неверное значение для обновления")
                    store.set_store_data(store_data)
                    return
            raise ValueError(f"Сделка с id: {id} не найдена")