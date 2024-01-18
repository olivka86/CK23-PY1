# TODO Напишите функцию для поиска индекса товара

def find_item_index(item_list: list, item: str) -> int:
    for index, item_in_list in enumerate(item_list):
        if item == item_in_list:
            return index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")


