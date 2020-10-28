from tkinter import *

import random

from tkinter import messagebox

from word_list import words

from string import ascii_uppercase


game_running = True

while game_running:
    root = Tk()
    root.geometry("600x600")
    root.title("Andrew's Hangman")
    game_running = False

    #here I am going to display my letter board
    #that the user will choose letters from
    letter_x = 0.05
    letter_y = 0.8
    new_letter_x = 0.05
    letter_count = 0
    hidden = "*"
    for i in ascii_uppercase:
        if letter_count >= 13:
            letter_y = 0.845
            my_button = Button(root, text=i, fg="white", bg="#006699")
            my_button.place(relx =new_letter_x,rely = letter_y,width = 50)
            new_letter_x += .07
        else:
            asc_button = Button(root, text=i, fg="white",bg="#006699")
            asc_button.place(relx = letter_x,rely = letter_y,width = 50)
            letter_count +=1
            letter_x += .07
    #here I am ending my letter board


    #here I am going to get the random word that the
    #game is going to use and that the user is going to guess

    game_word = random.choice(words)

    #here I am going to display the words in a hidden fashion
    if len(game_word) <=5:
        game_letter_x = 0.4
        game_letter_y = 0.6

    elif len(game_word) == 6:
        game_letter_x = 0.38
        game_letter_y = 0.6

    elif len(game_word) == 7:
        game_letter_x = 0.35
        game_letter_y = 0.6

    elif len(game_word) > 7:
        game_letter_x = 0.3
        game_letter_y = 0.6

    else:
        game_letter_x = 0.25
        game_letter_y = 0.6


    for i in game_word:
        game_letter_label = Label(root, text=hidden, fg="black")
        game_letter_label.place(relx = game_letter_x, rely = game_letter_y)
        game_letter_label.config(font=("courier new",25))
        game_letter_x += 0.05
        
 
    word_list = ["Hello", "Basketball", "Doctor", "wingman"]
    game_word = random.choice(word_list)
        
    welcome_title = Label(
        root,
        text="Welcome To Hangman",
        fg="#cc6600"
    )

    welcome_title.config(
        font=("Courier", 25)
    )

    welcome_title.place(
        anchor="n",
        relx=0.5,
        rely=0.05
    )

    easy_button = Button(
        root,
        text = "Easy"
        
        
        
    )

    easy_button.place(
        relx = 0.15,
        rely = 0.18,
        width = 100
    )

    medium_button = Button(
        root,
        text = "Medium",
        
    )

    medium_button.place(
        relx = 0.4,
        rely = 0.18,
        width = 100
    )

    hard_button = Button(
        root,
        text = "Hard",
        
    )

    hard_button.place(
        relx = 0.65,
        rely = 0.18,
        width = 100
    )

    root.mainloop()
