from pathlib import Path

script_location = Path(__file__).absolute().parent 
file_location = script_location / 'Day5Input.txt'
file = file_location.open()

input_list = file.read().splitlines()
test_boarding_pass = 'FBFBBFFRLR'

def search_min(input_search):
	return (input_search)[0]
	# given a range, returns the min value


def search_max(input_search):
	return (input_search)[len(input_search) - 1]
	# given a range, returns the max value


def next_search(boarding_pass, i, input_search):
	current_min = search_min(input_search)
	current_max = search_max(input_search)
	# print(current_min)
	# print(current_max)
	if boarding_pass[i] == 'F' or boarding_pass[i] == 'L':
		new_search = list(range(current_min, ((current_min + current_max + 1) // 2)))
	if boarding_pass[i] == 'B' or boarding_pass[i] == 'R':
		new_search = list(range(((current_min + current_max + 1) // 2), current_max + 1))
	return new_search
	# given a boarding pass, an index, and a range, next_search
	# will return a new range according to boarding_pass[index]

initial_search = list(range(0,128))
# # test:
# print(next_search(test_boarding_pass, 4, search_5))

def row_number(boarding_pass):
	initial_search = list(range(0,128))
	current_search = initial_search
	for i in range(0,7):
		current_search = next_search(boarding_pass, i, current_search)
		# print(current_search)
	return current_search


def column_number(boarding_pass):
	initial_search = list(range(0,8))
	current_search = initial_search
	for i in range(7,10):
		current_search = next_search(boarding_pass, i, current_search)
	return current_search


def seat_id(boarding_pass):
	return (row_number(boarding_pass)[0] * 8) + column_number(boarding_pass)[0]

def find_max(data):
	current_max = 0
	for boarding_pass in data:
		if seat_id(boarding_pass) >= current_max:
			current_max = seat_id(boarding_pass)
	return current_max

def list_seat_ids(data):
	seat_id_list = []
	for boarding_pass in data:
		seat_id_list.append(seat_id(boarding_pass))
	seat_id_list.sort()
	# print(seat_id_list)
	return seat_id_list


def find_missing(data):
    start, end = data[0], data[-1]
    return sorted(set(range(start, end + 1)).difference(data))

listed_seat_ids = list_seat_ids(input_list)

def find_seat(data):
	return find_missing(data)

print(find_seat(listed_seat_ids))