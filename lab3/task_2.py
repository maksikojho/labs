# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, sep=','):
    l1 = first_group.split(sep=sep)
    l2 = second_group.split(sep=sep)
    same_names = set(l1) & set(l2)
    return sorted(same_names)



participants_first_group = "Иванов|Сидоров|Петров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

result = find_common_participants(participants_first_group, participants_second_group, sep='|')
print(result)
