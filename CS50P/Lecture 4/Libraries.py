"""
Lecture 4 of CS50P course.
Reviewing libraries.
"""

#Libraries - reusable modules, import with "import"

#Random

import random

#random.choice(seq) - picks randomly from a list
coin = random.choice(["heads", "tails"])
print(coin)

#from - import only specific function (saves resources)
from random import choice
coin = choice(["heads", "tails"])

#random.randint(a, b) - random int between a and b
number = random.randint(1, 10)

#random.shuffle(x) - shuffles list IN PLACE, no return value
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

#Statistics

import statistics

#statistics.mean(list) - average
print(statistics.mean([100, 90]))

#Command-Line Arguments

import sys

#sys.argv - list of what user typed; [0] = script name, [1] = first arg

#Handle missing arg
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

#sys.exit() - exit with error message, keeps validation separate from logic
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

#Slice

#sys.argv[1:] - skip argv[0] (script name), iterate over the rest
for arg in sys.argv[1:]:
    print("hello, my name is", arg)

#Packages

#Third-party libraries installed via: pip install <package>
#PyPI (pypi.org) - repository of all available packages

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

#APIs

#requests - lets Python behave like a web browser (pip install requests)
#JSON - text-based format for exchanging data between applications

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)

#json.dumps(..., indent=2) - pretty-print JSON
print(json.dumps(response.json(), indent=2))

#Iterate over results
for result in response.json()["results"]:
    print(result["trackName"])

#Making Your Own Libraries

#Create sayings.py with reusable functions, then import from it
#def hello(name):
#    print(f"hello, {name}")

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
