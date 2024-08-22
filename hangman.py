import random 

#Print logo
from hangman_art import logo
print(logo)

#Variable to keep a track of lives
lives = 6
end_of_game = False

#Choose a random word from a list of words
from hangman_wordlist import word_list
chosen_word = random.choice(word_list)
print(f"Pssss.. The chosen word is {chosen_word}.")
word_length = len(chosen_word)

#Display
display = []
for _ in range(word_length):
    display += "_" 

#Take input for a letter
while not end_of_game:

  guess =  input("Guess a letter : ").lower()

  if guess in display:
    print(f"You've already guessed {guess}")

  for positions in range(word_length):
    letter = chosen_word[positions]

    if letter == guess:
      display[positions] = letter
    
  if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
          end_of_game = True
          print("You lose.")

  print(f"{' '.join(display)}")

  if "_" not in display:
        end_of_game = True
        print("You won.")                     

  from hangman_art import stages
  print(stages[lives])

