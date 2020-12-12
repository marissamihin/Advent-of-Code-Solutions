from pathlib import Path
import string

alphabet_list = list(string.ascii_lowercase)

script_location = Path(__file__).absolute().parent 
file_location = script_location / 'Day6Input.txt'
file = file_location.open()

input_list = file.read()

def group_parser(raw_list):
	raw_list = input_list.split("\n\n")
	parsed_list = []
	for i in range(len(raw_list)):
		parsed_line = raw_list[i].replace("\n", " ").split()
		parsed_list.append(parsed_line)
	return parsed_list


parsed_list = group_parser(input_list)
#Now the data is broken into lists, where each list represents a single group
#the number of items in each list represents the number of people in the group
#each item represents the questions to which the person answered yes

def group_reader(group):
	#takes in a list (representing a group), return a new list containing:
	#[(number of people in group), (number of questions to which they answered yes)]
	#the second element of the returned list accounts for repeats
	size = len(group)
	yes_letters = []
	all_yes_letter_count = 0
	for person in group:
		for answer in range(len(person)):
			yes_letters += person[answer]
	for letter in alphabet_list:
		letter_count = 0
		for person in group:
			for i in range(len(person)):
				if letter == person[i]:
					letter_count += 1
		if letter_count == len(group):
			all_yes_letter_count += 1
	return all_yes_letter_count

# test group_reader
# testgroup1 = parsed_list[0]
# testgroup2 = parsed_list[1]
# testgroup3 = parsed_list[2]
# testgroup4 = parsed_list[3]
# testgroup5 = parsed_list[4]
# print(group_reader(input_list))

# def read_all_groups(data):
# 	parsed_data = []
# 	for group in data:
# 		parsed_data += [group_reader(group)]
# 	return parsed_data

# read_groups = read_all_groups(parsed_list)

def sum_all_answers(data):
	answer_count = 0
	for parsed_group in data:
		answer_count += group_reader(parsed_group)
	return answer_count

print(sum_all_answers(parsed_list))
