import random
from assets import word_list
import assets

#we work with words as lists until we need to print them as strings, should make it a lot easier
def select_random_word(words):
    #select word with random index based on length of list
    selected_word = words[random.randint(0, len(words) - 1)]
    return list(selected_word)

#create underscored version of list based on length of selected word
def underscore_word(chosen_word):
    chosen_word_list = list(chosen_word)
    underscored_list = []
    for char in range(len(chosen_word_list)):
        underscored_list.append('_')
    return underscored_list

#check if letter exists in word
def letter_exists_in_word(letter, word):
    nr_occurrences = word.count(letter)
    if nr_occurrences > 0:
        return True
    else:
        return False

#
def stringify(input_list):
    stringified_list = ''.join(input_list)
    return stringified_list

# list comprehension with range() function
# https://www.geeksforgeeks.org/python/python-all-occurrences-of-substring-in-string/
def find_occurrences(string, substring):
    positions = [i for i in range(len(string)) if string.startswith(substring, i)]
    return positions


print('Welcome to Hangman game')
#the word to guess
word_to_guess = select_random_word(word_list)
#current state of underscored word, globally stored
current_state_underscore = underscore_word(word_to_guess)

#game logic

player_won = False
lives = 6
while lives > 0 and not player_won:

    print('Lives: ' + str(lives) + '/6')
    match lives:
        case 6:
            print(assets.full_health)
        case 5:
            print(assets.five_lives)
        case 4:
            print(assets.four_lives)
        case 3:
            print(assets.three_lives)
        case 2:
            print(assets.two_lives)
        case 1:
            print(assets.one_life)

    print(stringify(current_state_underscore))
    print()
    print('Make your guess')
    user_input = input()

    if letter_exists_in_word(user_input, word_to_guess):
        occurrences = find_occurrences(stringify(word_to_guess), user_input)
        for occurrence in occurrences:
            current_state_underscore[occurrence] = user_input
        print('Correct')

    else:
        print('Wrong')
        lives -= 1

    if current_state_underscore == word_to_guess:
        player_won = True
        print(f'You guessed the word {stringify(current_state_underscore)}, yay')


    if lives < 1:
        print(assets.dead)
        print(f'You died, the word was {stringify(word_to_guess)}')