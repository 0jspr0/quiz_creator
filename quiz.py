class quiz:
	def load(self):
		with open("quiz.txt", "r") as file:
			lines = file.readlines()