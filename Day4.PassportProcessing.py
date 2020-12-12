from pathlib import Path

script_location = Path(__file__).absolute().parent 
file_location = script_location / 'Day4Input.txt'
file = file_location.open()

input_list = file.read()

def credentials_parser(l):
	raw_list = l.split("\n\n")
	parsed_list = []
	for i in range(len(raw_list)):
		parsed_line = raw_list[i].replace("\n", " ").split()
		parsed_list.append(parsed_line)
	return parsed_list

valid_birth_year = range(1920, 2003)
valid_issue_year = range(2010, 2021)
valid_exp_year = range(2020, 2031)
valid_height_in = range(59, 77)
valid_height_cm = range(150, 194)
valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
hair_color_char = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def valid_hair_color_check(l):
	split_hairs = list(l[5:])
	if not(l[4] == "#"):
		return False
	for i in split_hairs:
		if not(i in hair_color_char):
			return False
	else:
		return True 


def valid_passport_id_check(l): 
	if not (len(l[4:])) == 9:
			return False
	for i in range(len(l[4:])):
		if i not in range(0,9):
			return False
	else:
		return True

def credentials_validator(l):
	fields_present = 0
	req_fields = 7
	valid_credentials = []
	for i in range(len(l)):
		key = l[i][0:3]
		if key == "byr":
			if int(l[i][4:]) in valid_birth_year:
				fields_present += 1
				# print('Birth year is good!')
		if key == "iyr":
			if int(l[i][4:]) in valid_issue_year:
				fields_present += 1	
				# print('Issue year is good!')
		if key == "eyr":
			if int(l[i][4:]) in valid_exp_year:
				fields_present += 1
				# print('Expiration year is good!')
		if key == "hgt":
			if (l[i][-2:]) == "in":
				if int(l[i][4:-2]) in valid_height_in:
					fields_present += 1
					# print('Height is good! (in)')
			if (l[i][-2:]) == "cm":
				if int(l[i][4:-2]) in valid_height_cm:
					fields_present += 1
					# print('Height is good! (cm)')
		if key == "hcl":
			if l[i][4] == "#" and len(l[i][5:]) == 6:
				if valid_hair_color_check(l[i]):
					fields_present += 1
					# print('Hair color is good!')
		if key == "ecl":
			if l[i][4:] in valid_eye_colors:
				fields_present += 1
				# print('Eye color is good!')
		if key == "pid":
			if valid_passport_id_check(l[i]):
				fields_present += 1
				# print('Passport ID is good!')
	if req_fields == fields_present:
		valid_credentials.append(l)
	return valid_credentials

def check_all(l):
	count = 0
	for line in l:
		if credentials_validator(line):
			count += 1
	return count


parsed_list = credentials_parser(input_list)
test_1 = parsed_list[0]
test_2 = parsed_list[1]
test_3 = parsed_list[2]
test_4 = parsed_list[3]
print(check_all(parsed_list))

# valid_passports = check_all(parsed_list)