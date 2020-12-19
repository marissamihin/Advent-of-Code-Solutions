from pathlib import Path
import string

input_list = Path("Day9Input.txt").resolve().read_text()

def data_parser(raw_list):
	split_lines = [line.split() for line in raw_list.splitlines()]
	return split_lines


def sum_search(search_number, main_list):
	start_interval = main_list.index(search_number) - 25
	end_interval = main_list.index(search_number)
	search_interval = main_list[start_interval:end_interval]
	for first_number in search_interval:
		for second_number in search_interval:
			if not(second_number == first_number):
				if (int(first_number[0]) + int(second_number[0]) == int(search_number[0])):
					return True
	print(search_number, 'is not valid!')
	return False


def find_interval(search_number, main_list):
	for bottom in main_list:
		for top in main_list:
			bottom_index = main_list.index(bottom)
			top_index = main_list.index(top)
			interval = (main_list[bottom_index:top_index+1])
			interval_sum = sum(interval)
			if interval_sum == search_number:
				return min(interval) + max(interval)




parsed_data = data_parser(input_list)
preamble = parsed_data[0:25]
postamble = parsed_data[25:]
for number in postamble:
	sum_search(number, parsed_data)

numbers = [int(x[0]) for x in parsed_data]
#FINALLY realized I could use list comprehension to turn the elements parsed_data into
#numbers instead of strings. but I already wrote sum_search using the string version of parsed_data
#and I'm feeling too lazy to go back and change it

#but hey! the code works!
invalid_number = 400480901
search_list = numbers[:numbers.index(invalid_number)]
print(find_interval(invalid_number, search_list))