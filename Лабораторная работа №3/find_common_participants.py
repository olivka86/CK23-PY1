# TODO Напишите функцию find_common_participants

def find_common_participants(first_group: str, second_group: str, separator: str = ',') -> list[str]:
    common_participants = set()
    for first in first_group.split(separator):
        for second in second_group.split(separator):
            if first == second:
                common_participants.add(first)

    return sorted(common_participants)


participants_first_group = "Иванов|Сидоров|Петров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, '|'))
