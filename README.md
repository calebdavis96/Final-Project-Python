# Final-Project-Python

## What:
The purpose of this project is to create a game of hangman in which the user has to guess characters of a word that has randomly been pulled out of a word bank.

## Why:
I thought this would be an interesting way to test my python skills, and I was very interested by the game of battleship we set up in Codecademy so i decided to do my own. There are plenty of codes for a hangman game online, but many have small flaws and for my game I would like to have it as polished as possible so that someone with no knowledge of python at all could sit down and play without issue.

## How:
First, I found a random word bank generator online and copied a large wordbank and formatted it correctly.I then imported the "random" module so that the game would choose a random word from the list every time the game started. Next I set up a greeting and had the user input their name.I then set up an empty set for guesses and set number of turns to 10, but turns will not count if the guess is correct. I then set up a "while" loop with a nested "for" loop that prints an underscore for each character that is not in the list of guesses. For each underscore, a 1 is then added to the "failed" variable. So when this failed variable is equal to zero, the player has won and a break is inserted to end the game here. I then set up a "while" loop to allow characters to be input for guesses and converted to lower case to avoid case problems. Every guess is added to the "guesses" variable and if the guess is not in the word, "Wrong" is printed and the number of guesses is also printed. When "turns" equals zero, the mystery word is revealed and the game ends.

## Usage/Example:
The game is really just for fun, and could be modified for some educational use with a different word bank and slight changes to the code.

## References:
Special thanks to Z. Miller(Professor at University of North Georgia)
http://members.optusnet.com.au/charles57/Creative/Techniques/random_words.htm - Random word list
