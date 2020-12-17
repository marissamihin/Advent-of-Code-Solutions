from pathlib import Path
import string

input_list = Path("Day7Input.txt").resolve().read_text()
# thanks, charlie! 

# the goal of this exercise is to find out:
# how MANY bags each "shiny gold" bag must hold
# test data looks like:

# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.

# under these rules, shiny gold bags must contain 126 bags total.

def data_parser(raw_list):
	split_lines = [line.split() for line in raw_list.splitlines()]
	for line in split_lines:
		line.remove('contain')
		line.remove('bags')
		for i in range(len(line)):
			if 'bag,' in line:
				line.remove('bag,')
			if 'bags,' in line:
				line.remove('bags,')
		line.pop(-1)
	return split_lines


def Convert_string_to_dictionary(lst):
	main_dict = {}
	for line in lst:
		sub_bag_list = line[2:]
		sub_bag_types = int(len(sub_bag_list) / 3)
		sub_bags = []
		for i in range(sub_bag_types):
			sub_bags += [sub_bag_list[i*3:(i+1)*3]]
		res_dct = {(line[0], line[1]): sub_bags}
		main_dict.update(res_dct)
	return main_dict


def bag_count(bag, main_dict):
	count = 0
	# print(bag, 'this is the bag')
	sub_bags = main_dict[bag]
	if len(sub_bags) < 1:
		print('end of this bag')
		return 1	
	print(sub_bags)
	for i in range(0, len(sub_bags)):
		sub_bag = sub_bags[i]
		count += int(sub_bag[0])*bag_count(tuple(sub_bag[1:]), main_dict)
	return count


#no errors! but I'm getting 0 for some reason?

parsed_data = data_parser(input_list)
print(parsed_data[0])
dictionary_data = Convert_string_to_dictionary(parsed_data)
shiny_gold = ('shiny', 'gold')
print(shiny_gold)
print(bag_count(shiny_gold, dictionary_data))