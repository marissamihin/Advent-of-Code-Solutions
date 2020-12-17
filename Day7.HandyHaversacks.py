from pathlib import Path
import string

input_list = Path("Day7Input.txt").resolve().read_text()
# thanks, charlie! 

# ************************* RAW DATA PARSING **********************************

# starting over with dictionaries

def data_parser(raw_list):
	#takes in all of the data, splits each line into lists
	return [line.split() for line in raw_list.splitlines()]

def Convert_to_dictionary(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

parsed_data = data_parser(input_list)
dictionary_data = Convert_to_dictionary(parsed_data)
print(dictionary_data)

