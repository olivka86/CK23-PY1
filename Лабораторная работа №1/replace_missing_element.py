numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

sum_of_numbers = 0
digits_amount = len(numbers)
none_index = 0

for index, num in enumerate(numbers):
    if num is not None:
        sum_of_numbers += num
    else:
        none_index = index

average = sum_of_numbers / digits_amount
numbers[none_index] = average

print("Измененный список:", numbers)