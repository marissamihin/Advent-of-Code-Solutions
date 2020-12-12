from pathlib import Path

script_location = Path(__file__).absolute().parent 
file_location = script_location / 'Day3Input.txt'
file = file_location.open()

input_list = file.read().splitlines()

def tree_count(l):
	count = 0
	for i in range(len(l)):
		if i % 2 == 0:
			if l[i][(int(i/2) % 31)] == "#":
				count += 1
	return count


print(tree_count(input_list))