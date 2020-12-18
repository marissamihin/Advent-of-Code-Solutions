from pathlib import Path
import string

input_list = Path("Day8Input.txt").resolve().read_text()
# print(repr(input_list))
# print(input_list)

# IT WORKS!

# for full instructions, visit https://adventofcode.com/2020/day/8

# currently input text is the test data:

# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6

# value of the accumulator before the code repeats itself should be 5.

# BEGIN PARSING

def data_parser(raw_list):
	split_lines = [line.split() for line in raw_list.splitlines()]
	return split_lines


def make_master(data):
	for line in data:
		lindex = data.index(line)
		line.append(lindex)
	return data


# def convert_to_dictionary(lst):
# 	main_dict = {}
# 	for line in lst:
# 		print(lst.index(line))
# 		res_dct = {lst.index(line): [line[0], line[1]]}
# 		main_dict.update(res_dct)
# 	return main_dict


def executor(index, main_list):
	# given an index and a list, returns (index change, accumulator change)
	op = main_list[index]
	if op[0] == 'nop':
		return (1, 0)
	if op[0] == 'acc':
		# print(op[1], 'should be added once')
		return (1, op[1])
	if op[0] == 'jmp':
		return (op[1], 0)


def run_code(main_list):
	used_indexes = []
	(current_index, accumulator) = (0,7)
	while not (current_index in used_indexes):
		used_indexes.append(current_index) # collection of indexes of operations we've already visited
		# print(used_indexes)
		current_index += int(executor(current_index, main_list)[0])
		# print(current_index) #changing the index based on the current rule
		if current_index == 648:
			print('Found it!')
			print(accumulator)
			return True
		elif not(current_index in used_indexes): #checking if we're revisiting an operation
			# print(int(executor(current_index, main_list)[1]), 'add this')
			accumulator += int(executor(current_index, main_list)[1])
			# print(accumulator, 'is accumulated') #if not, then we do the operation and proceed
		else:
			# print(main_list[current_index], 'this is the end.')
			return False #if we are, then the function ends and we get the accumulator value


def switch_op(op):
	# given an operation: if it's nop or jmp, switch. if not, return nothing
	if op[0] == "nop":
		op[0] = "jmp"
		return op
	if op[0] == "jmp":
		op[0] = "nop"
		return op
	else:
		print('Error! Not a nop or jump')


def op_search(main_list):
	current_index = 0
	while not(run_code(main_list)):
		for line in main_list:
			if line[0] == "jmp" or line[0] == "nop":
				line = switch_op(line)
				current_index = line[2]
			if not(run_code(main_list)):
				if line[0] == "jmp" or line[0] == "nop":
					line = switch_op(line)
					current_index = line[2]



parsed_data = data_parser(input_list)
master_list = make_master(parsed_data)
op_search(master_list)
# print(run_code(master_list))
