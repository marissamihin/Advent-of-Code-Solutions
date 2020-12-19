from pathlib import Path
import string

input_list = Path("Day9Input.txt").resolve().read_text()

def data_parser(raw_list):
	split_lines = [line.split() for line in raw_list.splitlines()]
	return split_lines


def make_master(data):
	for line in data:
		lindex = data.index(line)
		line.append(lindex)
	return data


def sum_search(start_index, line, main_list):
	# given a line, returns "True" if there exists two lines in the main_list that sum to it
	stop = int(line[0])
	search_index = 0
	for index in range(stop):
		if int(main_list[search_index][1]) + int(main_list[index][1]) == stop:
			return True
	search_index += 1
	if search_index == stop:
		print(main_list[search_index], 'is invalid!')
		return False
	else:
		sum_search(search_index, line, main_list)


def find_valid(main_list):
	preamble = main_list[0:25]
	for index in range(25, len(main_list)):
		line = main_list[index]
		if not(sum_search(index, line, main_list)):
			print(main_list[search_index], 'is invalid!')


parsed_data = data_parser(input_list)
master_list = make_master(parsed_data)
find_valid(master_list)