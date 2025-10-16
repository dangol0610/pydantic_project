from files.task2.test_validate_call import test_validate_call
from files.task3.store import DealsStore, ConnectionStore
from files.task3.repository import DealsRepository
from files.task3.schemas import Deal, User

from const import user_dict1, user_dict2, deal_dict1, deal_dict2, deal_dict_wrong
from settings.settings import settings

#task1
print(settings.db_url)

#task2
test_validate_call()

# task 3
store = DealsStore()
connection = ConnectionStore()
repository = DealsRepository(store, connection)

deals_to_create = [Deal(**deal_dict1), Deal(**deal_dict2), deal_dict_wrong]

repository.create_deal(deals_to_create)
print(repository.get_deals())
repository.update_deal(1, User(**user_dict1))
repository.update_deal(2, User(**user_dict2))
print(repository.get_deal(1))
print(repository.get_deals_dict())
