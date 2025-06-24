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
	answers = []
	answer_number = ((random_number - 1) * 6) + 1
	for i in range(4):
		answer_number += 1
		answer = lines[answer_number - 1]
		answers.append(answer)
	for answer in answers:
		print(answer)

def load_correct_answer(random_number, lines):
	correct_answer_number = ((random_number - 1) * 6) + 6
	correct_answer = lines[correct_answer_number - 1].replace("Correct answer: ", "")[:1]
	return correct_answer

def input_your_answer():
	your_answer = input("\nWhat is your answer? (a, b, c, or d)\n")
	return your_answer

def check_if_your_answer_is_correct(your_answer, correct_answer):
	if your_answer == correct_answer:
		print("Your answer is correct!")
	else:
		print("Your answer is incorrect!")
		print(f"Correct answer: {correct_answer}")

def load_quiz(quiz_file):
	lines, random_number = initialize(quiz_file)
	load_question(random_number, lines)
	load_answers(random_number, lines)
	correct_answer = load_correct_answer(random_number, lines)
	your_answer = input_your_answer()
	check_if_your_answer_is_correct(your_answer, correct_answer)