import random
#here is the logic of a hangman game
#add words if you choose to do so

word_list = ['dog', 'cat', 'kitty' 'justin']
guess_the_word = random.choice(word_list)
user_answer = []

def mygame(guess_the_word, user_answer):

    lives = 5
    while lives > 0:
        hidden = [i if i in user_answer else '-' for i in guess_the_word]
        print('current word: ', ''.join(hidden))
        print('lives: {}'.format(lives))

        if '-' not in hidden:
            print("Congragulations you guessed the correct word which was: {}".format(guess_the_word))
            return

        user_guess = input("Guess a letter: ")
        if user_guess in guess_the_word and user_guess not in user_answer:
            user_answer.append(user_guess)
        elif user_guess in user_answer:
            print("This has already been guessed")
        else:
            user_answer.append(user_guess)
            lives -= 1
            print("Not in the word sorry -1 life")

    print(" ")
    if lives == 0:
        print("I am sorry you have lost the game better luck next time")
    else:
        print('congrats my man or lady you won')

mygame(guess_the_word, user_answer)

