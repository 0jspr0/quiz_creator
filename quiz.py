import random

def initialize(quiz_file):
	with open(quiz_file, "r") as file:
		lines = file.readlines()
	number_of_entries = int(len(lines) / 6)
	random_number = random.randrange(1, 	number_of_entries + 1)
	for line in range(len(lines)):
		lines[line] = lines[line][:-1]