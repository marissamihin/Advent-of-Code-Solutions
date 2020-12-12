from pathlib import Path

script_location = Path(__file__).absolute().parent 
file_location = script_location / 'Day2inputAOC.txt'
file = file_location.open()

input_list = file.read().splitlines()

test_list = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

def password_parser(l):
	new_list = []
	for string in l:
		string_list = string.split(" ")
		new_list.append(string_list)
	return new_list


parsed_list = password_parser(input_list)

def password_validator(l):
	position_1 = int(l[0].split("-")[0])
	position_2 = int(l[0].split("-")[1])
	req_letter = list(l[1])[0]
	password = list(l[2])
	letter_count = 0
	if password[(position_1 - 1)] == req_letter and password[(position_2 - 1)] == req_letter:
		return False
	elif password[(position_1 - 1)] == req_letter or password[(position_2 - 1)] == req_letter:
		return True
	else:
		return False

def check_all(l):
	count = 0
	for line in l:
		if password_validator(line):
			count += 1
	return count

print(check_all(parsed_list))