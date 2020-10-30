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

    def letter_click(letter_text_color):
        letter_text_color = "red"


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

    hidden ="*"
    for i in game_word:
        game_letter_label = Label(root, text=hidden, fg="black")
        game_letter_label.place(relx = game_letter_x, rely = game_letter_y)
        game_letter_label.config(font=("courier new",25))
        game_letter_x += 0.05
        

 
    word_listt = ["Hello", "A"]
    game_word = random.choice(word_listt)

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


    #creation of buttons from a-z

    a_button = Button(root, text="A", width = 5,)
    a_button.place(relx=0.15,rely=0.8)

    b_button = Button(root, text="B", width = 5)
    b_button.place(relx=0.225,rely=0.8)

    c_button = Button(root, text="C",width=5)
    c_button.place(relx=0.3,rely=0.8)

    d_button = Button(root, text="D", width = 5)
    d_button.place(relx=0.375,rely=0.8)

    e_button = Button(root, text="E", width = 5)
    e_button.place(relx=0.45,rely=0.8)

    f_button = Button(root, text="F", width = 5)
    f_button.place(relx=0.525,rely=0.8)

    g_button = Button(root, text="G", width = 5)
    g_button.place(relx=0.6,rely=0.8)

    h_button = Button(root, text="H", width = 5)
    h_button.place(relx=0.675,rely=0.8)

    i_button = Button(root, text="I", width = 5)
    i_button.place(relx=0.75,rely=0.8)

    j_button = Button(root, text="J", width = 5)
    j_button.place(relx=0.15,rely=0.844)

    k_button = Button(root, text="K", width = 5)
    k_button.place(relx=0.225,rely=0.844)

    l_button = Button(root, text="L",width=5)
    l_button.place(relx=0.3,rely=0.844)

    m_button = Button(root, text="M", width = 5)
    m_button.place(relx=0.375,rely=0.844)

    n_button = Button(root, text="N", width = 5)
    n_button.place(relx=0.45,rely=0.844)

    o_button = Button(root, text="O", width = 5)
    o_button.place(relx=0.525,rely=0.844)

    p_button = Button(root, text="P", width = 5)
    p_button.place(relx=0.6,rely=0.844)

    q_button = Button(root, text="Q", width = 5)
    q_button.place(relx=0.675,rely=0.844)

    r_button = Button(root, text="R", width = 5)
    r_button.place(relx=0.75,rely=0.844)

    s_button = Button(root, text="S", width = 5)
    s_button.place(relx=0.15,rely=0.888)

    t_button = Button(root, text="T", width = 5)
    t_button.place(relx=0.225,rely=0.888)

    u_button = Button(root, text="U",width=5)
    u_button.place(relx=0.3,rely=0.888)

    v_button = Button(root, text="V", width = 5)
    v_button.place(relx=0.375,rely=0.888)

    w_button = Button(root, text="W", width = 5)
    w_button.place(relx=0.45,rely=0.888)

    x_button = Button(root, text="X", width = 5)
    x_button.place(relx=0.525,rely=0.888)

    y_button = Button(root, text="Y", width = 5)
    y_button.place(relx=0.6,rely=0.888)

    z_button = Button(root, text="Z", width = 5)
    z_button.place(relx=0.675,rely=0.888)

    z_button = Button(root, text="*", width = 5)
    z_button.place(relx=0.75,rely=0.888)

    #end of the creation of the buttons from a-z
    


    root.mainloop()
