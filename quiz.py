import random

def initialize(quiz_file):
	with open(quiz_file, "r") as file:
		lines = file.readlines()