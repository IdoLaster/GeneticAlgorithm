# Genetic Algorithm
A basic genetic algorithm written in python that meant to "find" a word.
This is only support letters (a-z, A-Z).\
There is a option to output some inforamtion as json in this format:
```
{
	GENERATION_NUMBER: 
	{
		"average_fitness": AVERAGE_FITNESS,
		"best": ["BEST_AS_STRING", BEST_FITNESS]
	}
}
```

### Usage:

```
$ python main.py --help
```

```
usage: main.py [-h] -w WORD [-s GENERATION_SIZE] [-b AMOUNT_OF_BEST]
               [-l AMOUNT_OF_LUCKY] [-c MUTATION_CHANCE] [-j JSON] [-v]

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
  -j JSON, --json JSON  the file to output the result as json.
  -v, --visualization   Set this flag if you want the data to be visualized
                        after the program ran.
```


### Examples:
For the following command:
```
python main.py -w Bunny
```

We will get:
```
=============
GENERATION 1
=============
Imnbs => 20
RanwM => 20
uPsFy => 20
nCZdy => 20
uTSdy => 20
BqADW => 20
chnwD => 20
BPsDO => 20
uanFD => 20
uenAl => 20
chRbW => 0
tTzgD => 0
feRZW => 0
cCSlW => 0
tezAF => 0
ImZbM => 0
tkAis => 0
IPsbA => 0
flZPl => 0
ukADM => 0
*----------*
=============
GENERATION 2
=============
RanwF => 20
Imnbs => 20
flZdy => 20
ueSdy => 20
IenAF => 20
nCZdy => 20
nCzAy => 20
ImZOs => 0
Imsbs => 0
teDAF => 0
...
=============
GENERATION 63
=============
hunny => 80
Sunny => 80
munny => 80
Eunny => 80
punny => 80
pWnny => 60
munvy => 60
mmnny => 60
Sunnx => 60
hJnny => 60
...
=============
GENERATION 194
=============
Bunny => 100
Funny => 80
Lunny => 80
Xunay => 60
Fvnny => 60
LunnF => 60
Xvnny => 60
XunnF => 60
FunnF => 60
FunnR => 60
Fvnay => 40
yvnRy => 40
FunRv => 40
FvnnF => 40
FvVny => 40
*-----------*
```
This has been shorten because the log was like 800 lines.