"""
Lecture 4 of CS50P course.
Reviewing libraries, packages and APIs.
"""
 
#random
 
import random
 
coin = random.choice(["heads", "tails"])
print(coin)
 
number = random.randint(1, 10)
print(number)
 
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
 
#from - import only what you need (saves resources)
from random import choice
coin = choice(["heads", "tails"])
 
#statistics
 
import statistics
print(statistics.mean([100, 90]))
 
#command-line arguments
 
import sys
 
#sys.argv[0] = script name, sys.argv[1] = first argument
 
#Worse - throws IndexError if no argument given
#print("hello, my name is", sys.argv[1])
 
#Better - check length first, use sys.exit() to keep error handling separate
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
 
print("hello, my name is", sys.argv[1])
 
#slice
 
#sys.argv[1:] skips the first element (script name)
for arg in sys.argv[1:]:
    print("hello, my name is", arg)
 
#packages
 
#pip install cowsay
import cowsay
import sys
 
if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
 
#APIs
 
import requests
import json
import sys
 
if len(sys.argv) != 2:
    sys.exit()
 
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)
 
#Pretty print full JSON
print(json.dumps(response.json(), indent=2))
 
#Or just extract what you need
for result in response.json()["results"]:
    print(result["trackName"])
 
#Making my own library
 
#sayings.py
def hello(name):
    print(f"hello, {name}")
 
def goodbye(name):
    print(f"goodbye, {name}")
 
#say.py - importing from your own library
from sayings import goodbye
 
if len(sys.argv) == 2:
    goodbye(sys.argv[1])
