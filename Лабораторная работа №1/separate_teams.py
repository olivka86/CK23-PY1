list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

half_of_the_players = len(list_players) // 2

first_team = list_players[:half_of_the_players]
second_team = list_players[half_of_the_players:]

print(first_team)
print(second_team)