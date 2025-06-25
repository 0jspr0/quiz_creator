import quiz

def load_quiz(quiz_file):
	lines, random_number = initialize(quiz_file)
	load_question(random_number, lines)
	load_answers(random_number, lines)
	correct_answer = load_correct_answer(random_number, lines)
	your_answer = input_your_answer()
	check_if_your_answer_is_correct(your_answer, correct_answer)

load_quiz("quiz.txt")