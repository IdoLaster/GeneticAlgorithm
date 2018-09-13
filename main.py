import random
import string
import operator
import argparse

def generate_word(length):
	"""
	This function used to generate a random word in a given length.
	"""
	result = ""

	for i in xrange(length):
		result += random.choice(string.letters)
	return result

def fitness_function(corret_word, word):
	"""
	Fitness function - this function used to give a "score" for a word.
	"""
	if len(corret_word) != len(word):
		print "Length error."
		print corret_word + " | " + word
		return

	index = 0
	fitness = 0

	for letter in corret_word:
		if letter == word[index]:
			fitness += 1
		index += 1

	return fitness * 100 / len(corret_word)

def generate_first_generation(generation_size, correct_word):
	"""
	Generate first generation - this function used to generate a completely random generation
	we will be using it only once.
	"""
	result = []

	for i in xrange(generation_size):
		result.append(generate_word(len(correct_word)))

	return result

def evaluate_generation(generation, correct_word):
	"""
	Evaluate Generation - This function takes a generation and gives each individual is fitness.
	returns a list of tuples where the first item is the word and the second is the fitness.
	"""
	result = {}

	for individual in generation:
		result[individual] = fitness_function(correct_word, individual)

	return sorted(result.items(), key = operator.itemgetter(1), reverse=True)

def generation_selection(generation_evaluated, amount_of_best, amount_of_random):
	"""
	Generation Selection - this function takes the generation evaluated
	and returns only the few best one and a few random ones.
	"""
	result = []
	for i in xrange(amount_of_best):
		result.append(generation_evaluated[i][0])
	for i in xrange(amount_of_random):
		result.append(random.choice(generation_evaluated)[0])
	return result

def breed_child(mom, dad):
	"""
	Breed Child - This function takes 2 parents and breed a child,
	by taking a random letter from either one of the parents.
	"""
	child = ""
	for i in xrange(len(mom)):
		if int(random.random() * 100) < 50:
			child += mom[i]
		else:
			child += dad[i]
	return child

def generate_generation(parents, generation_size):
	"""
	Generate Generation - This is basiclly generating a new geeration using the breed child function.
	"""
	result = []
	for i in xrange(len(parents)/2):
		for j in xrange(generation_size/5):
			result.append(breed_child(parents[i], parents[len(parents) -1 -j]))
	return result


def mutate_word(word):
	"""
	Mutate word - This function mutating a word, it's picks a random
	index and changing it to random other letter.
	"""
	index_of_mutation = int(random.random()*len(word))
	random_letter = random.choice(string.letters)
	if index_of_mutation == 0:
		word = random_letter + word[1:]
	else:
		word = word[:index_of_mutation] + random_letter+ word[index_of_mutation+1:]
	return word

def mutate_generation(generation, chance):
	"""
	Mutate Generation - This repeats the mutate_word for each word in a generation by a chance
	(means there is only x chance of it to mutate a word.)
	"""
	for i in xrange(len(generation)):
		if random.random() * 100 < chance:
			mutated_word = mutate_word(generation[i])
			generation[i] = mutated_word
	return generation

def print_evaluated_generation(generation_evaluated, CORRECT_WORD):
	"""
	This function just prints an evaluated generation.
	"""
	for individual in generation_evaluated:
		print individual[0] + " => " + str(individual[1])
	print "*" + "-" * (len(CORRECT_WORD) + 5 + len(str(individual[1]))-1) + "*"

def main():
	# Setting up agruments parser.
	parser = argparse.ArgumentParser(description='This is a simple genetic algorithm using to find a word.')
	parser.add_argument("-w", "--word", required=True, help="This is the target word")
	parser.add_argument("-s", "--generation_size",type=int, default=20, help="This is the generation size")
	parser.add_argument("-b", "--amount_of_best", default=6, type=int, help="This is the amount of the best individuals to pick from each generation.")
	parser.add_argument("-l", "--amount_of_lucky", default=4, type=int, help="This is the amount of the lucky few individuals to pick from each generation.")
	parser.add_argument("-c", "--mutation_chance", default=25, type=int, help="This is the chance of word to get mutated (by percentage)")
	
	# Parsing the arguments.
	args = parser.parse_args()
	if args.amount_of_best + args.amount_of_lucky > args.generation_size:
		print "Amount of best and amount of luck should not be more then the generation size."
		return
	CORRECT_WORD = args.word
	GENERATION_SIZE = args.generation_size
	AMOUNT_OF_BEST = args.amount_of_best
	AMOUNT_OF_RANDOM = args.amount_of_lucky
	MUTATION_CHANCE = args.mutation_chance

	# Generating first generation
	generation = generate_first_generation(GENERATION_SIZE, CORRECT_WORD)
	generation_evaluated = evaluate_generation(generation, CORRECT_WORD)
	while generation_evaluated[0][1] != 100:
		"""
		Enterting the main loop:
		Here we simply calling all the functions until we get fitness of 100.
		We are calling in this order:
		1. First we are making a selection from the old generation of few of the best ones
		   And a couple of lucky ones
		2. We generate new generation using the seleced individuals as parents for the new ones.
		3. Mutate Generation so it will be a little different.
		4. Evaluate the generation.
		5. Repeat, Selection => generate newer generation => mutate => evaluate, until fitness 100.
		"""
		generation_selected = generation_selection(generation_evaluated, AMOUNT_OF_BEST, AMOUNT_OF_RANDOM)
		generation = generate_generation(generation_selected, GENERATION_SIZE)
		generation_mutated = mutate_generation(generation, MUTATION_CHANCE)
		generation_evaluated = evaluate_generation(generation_mutated, CORRECT_WORD)
		print_evaluated_generation(generation_evaluated, CORRECT_WORD)

if __name__ == "__main__":
    main()