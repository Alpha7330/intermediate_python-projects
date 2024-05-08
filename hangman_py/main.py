#Step 1 
import hangman_words
import hangman_art
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(hangman_words.word_list)
display=[]
lives=6
print(hangman_art.logo)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
for i in range(len(chosen_word)):
  display+="_"
while "_" in display:  
  guess =input("\nGuess a letter:\n").lower()
  print(display)
  for pos  in range(len(chosen_word)):
    letter = chosen_word[pos]
    if letter==guess:
      display[pos]=guess
  print(display)
  if guess not in display:
    lives-=1
    print(hangman_art.stages[lives])
    if lives==0:
       print("You lose")
       break  
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
if "_" not in display:
  print("You win")

