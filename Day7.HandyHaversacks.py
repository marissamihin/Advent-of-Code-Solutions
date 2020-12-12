from pathlib import Path
import string

alphabet_list = list(string.ascii_lowercase)

script_location = Path(__file__).absolute().parent 
file_location = script_location / 'Day7Input.txt'
file = file_location.open()

input_list = file.read()
print(input_list)

# ************************* RAW DATA PARSING **********************************

def data_parser(raw_list):
	#takes in all of the data, splits each line into lists
	raw_list = input_list.split("\n")
	parsed_list = []
	for i in range(len(raw_list)):
		parsed_line = raw_list[i].replace("\n", " ").split()
		parsed_list.append(parsed_line)
	return parsed_list


def get_sub_bags(rule):
	# input needs to be after the "contains" of a rule, so rule[4:]
	# given a rule, returns the list of list of bags it can contain
	sub_bags = []
	sub_bag_types = int(len(rule) / 4)
	for i in range(sub_bag_types):
			new_sub_bag = rule[1:3]
			sub_bags.append([new_sub_bag])
			if rule[4:]:
				rule = rule[4:]
			else: 
				break
	return sub_bags


def rule_parser(rule):
	# takes in one rule (a list) and returns:
	# first element is the bag to which the rule pertains
	# second element is a list containing [number, bag type]
	# ex. [vibrant lime, [['faded', 'gold'], ['plaid', 'aqua'], ['clear' 'black']]
	main_bag_type = rule[0:2]
	sub_bags = []
	remaining_bags = get_sub_bags(rule[4:])
	for i in range(len(remaining_bags)):
		sub_bags += remaining_bags[i]
	return [main_bag_type, sub_bags]


def parse_all(parsed_list):
	new_list = []
	for rule in parsed_list:
		new_list.append(rule_parser(rule))
	return new_list


#******************************* ALL PARSING IS DONE *******************
# Everything above this line takes in the raw data and returns each rule as:
# [main bag, [sub_bags]]
# ex.['vibrant', 'lime', [['faded', 'gold'], ['plaid', 'aqua'], ['clear' 'black']]
# none of the above functions are called again, the real work is the 4 below	


def can_directly_hold(rule):
	# tells you if this color bag can directly hold a shiny gold bag
	# input needs to be rule[0], rule[1:]
	main_bag = rule[0]
	sub_bags = rule[1:]
	if sub_bags == [[]]:
		return False
	for bag_type in sub_bags:
		if len(sub_bags) == 0:
			return False
		if bag_type[0] == ['shiny', 'gold']:
			return True
		else:
			return False


def rule_finder(bag_type, parsed_data):
	# given a bag type, will search through all of the parsed data
	# and return a rule in which that bag_type is the main_bag
	# input is a sub_bag, or ['adjective', 'color']
	for rule in parsed_data:
		if rule[0] == bag_type:
			return rule


def can_indirectly_hold(rule, input_data):
	# tells you if this color bag can INdirectly hold a shiny gold bag:
	# that is, can it hold a bag that CAN hold a shiny gold bag, etc.
	if can_directly_hold(rule):
		return True
	sub_bags = rule[1:][0]
	if sub_bags == [[]]:
		return False
	for sub_bag in sub_bags:
		if rule_finder(sub_bag, input_data):
			if can_indirectly_hold(rule_finder(sub_bag, input_data), input_data):
				return True
	return False


def count(input_data):
	# checks each rule in the input data, counts the number that can hold
	# shiny gold bags
	count = 0
	for rule in input_data:
		if can_indirectly_hold(rule, input_data):
			count += 1
	return count


# ACTUAL FUNCTION CALLS

parsed_list = data_parser(input_list)
parsed_rules = parse_all(parsed_list)
print(count(parsed_rules))


# TESTING

# TEST DATA:

# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# should get that there are 4 bags colors that work. 

# test_rule1 = parsed_list[0]
# test_rule2 = parsed_list[1]
# test_rule3 = parsed_list[2]
# test_rule4 = parsed_list[7]
# parsed_test_rule1 = rule_parser(test_rule1)
# parsed_test_rule2 = rule_parser(test_rule2)
# parsed_test_rule3 = rule_parser(test_rule3)
# parsed_test_rule4 = rule_parser(test_rule4)
# print(parsed_test_rule4)
# print(can_directly_hold(parsed_test_rule4))
# print(can_indirectly_hold(parsed_test_rule4, parsed_rules))
# print(count(parsed_rules))