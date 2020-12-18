from pathlib import Path
import string

input_list = Path("Day7Input.txt").resolve().read_text()
# thanks, charlie! 
# IT WORKS! thanks absolute-minimum!

# the goal of this exercise is to find out:
# how MANY bags each "shiny gold" bag must hold
# test data looks like:

# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.

# under these rules, shiny gold bags must contain 32 bags total.

# BEGIN PARSING

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


def convert_string_to_dictionary(lst):
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


# END PARSING

def bag_count(bag, main_dict):
	count = 0
	sub_bags = main_dict[bag]
	if len(sub_bags) < 1:
		return 1
	count += 1
	for bag in sub_bags:
		print(bag[1:], 'bags contain', bag_count(tuple(bag[1:]), main_dict), 'bags.')
		count += int(bag[0])*bag_count(tuple(bag[1:]), main_dict)
	return count

parsed_data = data_parser(input_list)
dictionary_data = convert_string_to_dictionary(parsed_data)
shiny_gold = ('shiny', 'gold')
print(shiny_gold)
print(bag_count(shiny_gold, dictionary_data) - 1)