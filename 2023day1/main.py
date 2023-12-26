import re

with open("calibration_doc.txt") as file:
    data = file.readlines()

numbers = []
for i in range(0,len(data)):
    re.findall(r'\d+', data[i])
    numbers.append(re.findall(r'\d+', data[i]))
print(numbers)

first_digit_list = []
for i in range(0,len(data)):
    first_digit = re.search(r'\d', data[i])
    first_digit_list.append(first_digit.group())
print(first_digit_list)

last_number_list = []
for i in range(0,len(numbers)):
    last_number = numbers[i][-1]
    last_number_list.append(last_number)
# print(numbers[2][-1])
# print(last_number_list)

last_digit_list = []
for i in range(0,len(last_number_list)):
    last_digit = last_number_list[i][len(last_number_list[i])-1]
    # last_digit = re.search(r'\d^0$', data[i])
    last_digit_list.append(last_digit)
print(last_digit_list)
# print(last_number_list[2][len(last_number_list[2])-1])
# last_number_list[i][len(last_number_list[i])-1]

# print(first_digit_list[0]+last_digit_list[0])
final_sum = 0
for i in range(0,len(last_digit_list)):
    new_number = first_digit_list[i] + last_digit_list[i]
    final_sum += int(new_number)
print(final_sum)
