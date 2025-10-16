from files.task3.schemas import DealType

user_dict1 = {
    'id': 1,
    'name': 'Daniil Golubev',
    'age': 23,
    'is_supervisor': False,
    'email': 'dangol0610@gmail.com',
    'phone_number': '+7 (962) 184-51-53'
} 
user_dict2 = {
    'id': 2,
    'name': 'Dmitriy Utkin',
    'age': 27,
    'is_supervisor': True,
    'email': 'du@gmail.com',
    'phone_number': '+7 (999) 123-12-34'
}

deal_dict1 = {
    'id': 1,
    'title_deal': 'Покупка квартиры',
    'comment': 'Дорого',
    'created_at': '2025-10-01',
    'persons_in_charge': [],
    'deal_type': DealType.purchase
}
deal_dict2 = {
    'id': 2,
    'title_deal': 'Продажа квартиры',
    'comment': 'Дорого',
    'created_at': '2025-10-15',
    'persons_in_charge': [],
    'deal_type': DealType.sale
}
deal_dict_wrong = {
    'id': 23,
    'title_deal': 'Продажа квартиры',
    'comment': 'Дорого',
    'created_at': 123.123,
    'persons_in_charge': [],
    'deal_type': True
}

