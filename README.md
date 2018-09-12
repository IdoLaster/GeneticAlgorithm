# Genetic Algorithm
A basic genetic algorithm written in python that meant to "find" a word. 

### Usage:

```
$ python main.py --help
```

```
usage: main.py [-h] -w WORD [-s GENERATION_SIZE] [-b AMOUNT_OF_BEST]
               [-l AMOUNT_OF_LUCKY] [-c MUTATION_CHANCE]

This is a simple genetic algorithm using to find a word.

optional arguments:
  -h, --help            show this help message and exit
  -w WORD, --word WORD  This is the target word
  -s GENERATION_SIZE, --generation_size GENERATION_SIZE
                        This is the generation size
  -b AMOUNT_OF_BEST, --amount_of_best AMOUNT_OF_BEST
                        This is the amount of the best individuals to pick
                        from each generation.
  -l AMOUNT_OF_LUCKY, --amount_of_lucky AMOUNT_OF_LUCKY
                        This is the amount of the lucky few individuals to
                        pick from each generation.
  -c MUTATION_CHANCE, --mutation_chance MUTATION_CHANCE
                        This is the chance of word to get mutated (by
                        percentage)
```