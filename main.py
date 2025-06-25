import quiz

def load_quiz(quiz_file):
	lines, random_number = quiz.initialize(quiz_file)
	quiz.load_question(random_number, lines)
	quiz.load_answers(random_number, lines)
	correct_answer = quiz.load_correct_answer(random_number, lines)
	your_answer = quiz.input_your_answer()
	quiz.check_if_your_answer_is_correct(your_answer, correct_answer)

load_quiz("quiz.txt")