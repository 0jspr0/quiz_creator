import random

def initialize(quiz_file):
	with open(quiz_file, "r") as file:
		lines = file.readlines()
	number_of_entries = int(len(lines) / 6)
	random_number = random.randrange(1, 	number_of_entries + 1)
	for line in range(len(lines)):
		lines[line] = lines[line][:-1]
	return lines, random_number

def load_question(random_number, lines):
	question_number = ((random_number - 1) * 6) + 1
	question = lines[question_number - 1].replace("Question: ", "")
	print(question)

def load_answers(random_number, lines):