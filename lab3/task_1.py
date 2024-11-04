
# TODO Напишите функцию для поиска индекса товара

def finder(list, item):
    result = None
    i = 0
    while i < len(list):
        result = i if item == list[i] else None
        if result is not None:
            break
        i += 1
    return result

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = finder(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
