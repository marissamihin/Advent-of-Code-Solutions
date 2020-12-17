from pathlib import Path
import string

input_list = Path("Day7Input.txt").resolve().read_text()
# thanks, charlie! 

# ************************* RAW DATA PARSING **********************************

# starting over with dictionaries....

def data_parser(raw_list):
	#takes in all of the data, splits each line into lists
	return [line.split() for line in raw_list.splitlines()]


def Convert_string_to_dictionary(lst):
	main_dict = {}
	for line in lst:
		sub_bags = tuple(line[4:])
		res_dct = {(line[0], line[1]): sub_bags}
		main_dict.update(res_dct)
	return main_dict


def bag_count(bag, main_dict):
	count = 0
	# print(bag, 'this is the bag')
	sub_bag_types = int(len(bag) / 4)
	# print(sub_bag_types)
	for i in range(0, sub_bag_types):
		sub_bag = main_dict[bag[((i*4) + 1):((i*4)+3)]]
		# print(sub_bag, 'this is the sub_bag')
		if bag[0] == 'no':
			return 1
		if sub_bag[0] == 'no':
			return 1
		if sub_bag[3] == 'bags.':
			return 1
		else:
			count += int(sub_bag[(i)*4])*bag_count(sub_bag, main_dict) 
	return count


# I keep getting an "IndexError: tuple index out of range" message
# and I think I understand WHY, but I'm not sure how to fix it...
# I may have to scrap the indexing and try some other way
# there's almost certainly a way to do this nicely....


parsed_data = data_parser(input_list)
dictionary_data = Convert_string_to_dictionary(parsed_data)
shiny_gold = dictionary_data[('shiny', 'gold')]
print(bag_count(shiny_gold, dictionary_data))