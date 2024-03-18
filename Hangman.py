import random
from hangman_word import word_list
from hangman_art import stages, logo
end_of_game = False
chosen_word = random.choice(word_list)
lives = 6

print(logo)

display = []
for i in chosen_word:
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You has entered {guess} that you have already guessed")

    index = 0
    for letter in chosen_word:
        if letter == guess:
            display[index] = guess
        index += 1

    if guess not in chosen_word:
        print(f"You has entered {guess} that is not in the word. You lose a life")
        lives -=1

    if lives == 0:
        print("You lose!!!")
        end_of_game = True

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!!!")
    print(stages[lives])