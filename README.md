# Genetic Algorithm
A basic genetic algorithm written in python that meant to "find" a word.
This is only support letters (a-z, A-Z).
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


### Examples:
For the following command:
```
python main.py -w Bunny -s 50 -b 15 -l 5 -c 50
```

We will get:
```
BzJcy => 40
YuFsQ => 20
TlnTh => 20
rVqoy => 20
NOnul => 20
zZSNy => 20
rmfoy => 20
vOntl => 20
NanhF => 20
fZSNy => 20
HuVgo => 20
BzJae => 20
JlSNy => 20
xjkdy => 20
QZSgy => 20
QOnTq => 20
QZhWy => 20
fufuC => 20
HuVkA => 20
BzJZv => 20
mmqoy => 20
jkSiy => 20
QZvNy => 20
BiJtl => 20
rmCoy => 20
HuSNu => 20
JuVEh => 20
BaFsv => 20
QZSNy => 20
rmqoy => 20
cOnTq => 20
fgzui => 0
RaFse => 0
KZvAc => 0
vghul => 0
zVCui => 0
xkiXh => 0
fKXLw => 0
fzJuC => 0
Jgvhh => 0
YkFiF => 0
RQfHC => 0
RZvIA => 0
NOIAA => 0
vHqtl => 0
gqhte => 0
xgiXj => 0
RHgiG => 0
NOiTj => 0
hYXLw => 0
Rngie => 0
fedWQ => 0
hlvhh => 0
RFGgq => 0
fedWA => 0
fEFsQ => 0
zqvXj => 0
hjXde => 0
fefWQ => 0
daFsF => 0
hYXLF => 0
feitl => 0
ROGWo => 0
*----------*
BuIcy => 60
BzJay => 40
Huqgy => 40
Bzfay => 40
...
*-----------*
Bunny => 100
Bunpy => 80
Bunvy => 80
Bunty => 80
Buniy => 80
BunRy => 80
Bunhy => 80
BunVy => 80
Bunly => 80
BunHy => 80
BunNy => 80
Bunqy => 80
Bunwy => 80
Bunuy => 80
...
*-----------*

```
This has been shorten because the log was like 800 lines.