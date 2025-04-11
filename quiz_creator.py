def create_quiz():
    while True:
    	question = input("Enter a question:\n")

        answers = {}
        for option in ['a', 'b', 'c', 'd']:
            answer = input(f"Enter answer option {option}:\n")
            answers[option] = answer