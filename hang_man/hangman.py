from tkinter import *

import random

from tkinter import messagebox

from word_list import words

from string import ascii_uppercase


game_running = True

while game_running == True:
    root = Tk()
    root.geometry("600x600")
    root.title("Andrew's Hangman")
    game_running = False

    letter_text_color = "black"
    #game is going to use and that the user is going to guess
    game_word = random.choice(words).upper()
    letters_guessed = []
    def letter_click(letter,letters_guessed):
        if letter == "A":
            a_button.config(state="disabled",bg="#909090")

        if letter == "B":
            b_button.config(state="disabled",bg="#909090")

        if letter == "C":
            c_button.config(state="disabled",bg="#909090")

        if letter == "D":
            d_button.config(state="disabled",bg="#909090")

        if letter == "E":
            e_button.config(state="disabled",bg="#909090")

        if letter == "F":
            f_button.config(state="disabled",bg="#909090")

        if letter == "G":
            g_button.config(state="disabled",bg="#909090")

        if letter == "H":
            h_button.config(state="disabled",bg="#909090")

        if letter == "I":
            i_button.config(state="disabled",bg="#909090")

        if letter == "J":
            j_button.config(state="disabled",bg="#909090")

        if letter == "K":
            k_button.config(state="disabled",bg="#909090")

        if letter == "L":
            l_button.config(state="disabled",bg="#909090")

        if letter == "M":
            m_button.config(state="disabled",bg="#909090")

        if letter == "N":
            n_button.config(state="disabled",bg="#909090")

        if letter == "O":
            o_button.config(state="disabled",bg="#909090")

        if letter == "P":
            p_button.config(state="disabled",bg="#909090")

        if letter == "Q":
            q_button.config(state="disabled",bg="#909090")

        if letter == "R":
            r_button.config(state="disabled",bg="#909090")

        if letter == "S":
            s_button.config(state="disabled",bg="#909090")

        if letter == "T":
            t_button.config(state="disabled",bg="#909090")

        if letter == "U":
            u_button.config(state="disabled",bg="#909090")

        if letter == "V":
            v_button.config(state="disabled",bg="#909090")

        if letter == "W":
            w_button.config(state="disabled",bg="#909090")

        if letter == "X":
            x_button.config(state="disabled",bg="#909090")

        if letter == "Y":
            y_button.config(state="disabled",bg="#909090")

        if letter == "Z":
            z_button.config(state="disabled",bg="#909090")

        letters_guessed.append(letter)

        #here I am going to display the words in a hidden fashion
        #then I am going to handle the input if the user
        #guesses the right letter, to be displayed
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

        for i in range(len(game_word)):
            if game_word[i] in letters_guessed:
                game_letter_label = Label(root, text=game_word[i], fg="black")
                game_letter_label.place(relx = game_letter_x, rely = game_letter_y)
                game_letter_label.config(font=("courier new",25))
                game_letter_x += 0.05
            else:
                game_letter_label = Label(root, text="*", fg="black")
                game_letter_label.place(relx = game_letter_x, rely = game_letter_y)
                game_letter_label.config(font=("courier new",25))
                game_letter_x += 0.05

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

    a_button = Button(root, text="A", width = 5, fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("A",letters_guessed))
    a_button.place(relx=0.15,rely=0.8)

    b_button = Button(root, text="B", width = 5, fg=letter_text_color,
                    bg="#ff944d",
                    command=lambda: letter_click("B",letters_guessed))
    b_button.place(relx=0.225,rely=0.8)

    c_button = Button(root, text="C",width=5, fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("C",letters_guessed))
    c_button.place(relx=0.3,rely=0.8)

    d_button = Button(root, text="D", width = 5, fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("D",letters_guessed))
    d_button.place(relx=0.375,rely=0.8)

    e_button = Button(root, text="E", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("E",letters_guessed))

    e_button.place(relx=0.45,rely=0.8)

    f_button = Button(root, text="F", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("F",letters_guessed))
    f_button.place(relx=0.525,rely=0.8)

    g_button = Button(root, text="G", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("G",letters_guessed))
    g_button.place(relx=0.6,rely=0.8)

    h_button = Button(root, text="H", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("H",letters_guessed))
    h_button.place(relx=0.675,rely=0.8)

    i_button = Button(root, text="I", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("I",letters_guessed))
    i_button.place(relx=0.75,rely=0.8)

    j_button = Button(root, text="J", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("J",letters_guessed))
    j_button.place(relx=0.15,rely=0.844)

    k_button = Button(root, text="K", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("K",letters_guessed))
    k_button.place(relx=0.225,rely=0.844)

    l_button = Button(root, text="L",width=5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("L",letters_guessed))
    l_button.place(relx=0.3,rely=0.844)

    m_button = Button(root, text="M", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("M",letters_guessed))
    m_button.place(relx=0.375,rely=0.844)

    n_button = Button(root, text="N", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("N",letters_guessed))
    n_button.place(relx=0.45,rely=0.844)

    o_button = Button(root, text="O", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("O",letters_guessed))
    o_button.place(relx=0.525,rely=0.844)

    p_button = Button(root, text="P", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("P",letters_guessed))
    p_button.place(relx=0.6,rely=0.844)

    q_button = Button(root, text="Q", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("Q",letters_guessed))
    q_button.place(relx=0.675,rely=0.844)

    r_button = Button(root, text="R", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("R",letters_guessed))
    r_button.place(relx=0.75,rely=0.844)

    s_button = Button(root, text="S", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("S",letters_guessed))
    s_button.place(relx=0.15,rely=0.888)

    t_button = Button(root, text="T", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("T",letters_guessed))
    t_button.place(relx=0.225,rely=0.888)

    u_button = Button(root, text="U",width=5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("U",letters_guessed))
    u_button.place(relx=0.3,rely=0.888)

    v_button = Button(root, text="V", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("V",letters_guessed))
    v_button.place(relx=0.375,rely=0.888)

    w_button = Button(root, text="W", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("W",letters_guessed))
    w_button.place(relx=0.45,rely=0.888)

    x_button = Button(root, text="X", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("X",letters_guessed))

    x_button.place(relx=0.525,rely=0.888)

    y_button = Button(root, text="Y", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("Y",letters_guessed))
    y_button.place(relx=0.6,rely=0.888)

    z_button = Button(root, text="Z", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("Z",letters_guessed))
    z_button.place(relx=0.675,rely=0.888)

    star_button = Button(root, text="*", width = 5)
    star_button.place(relx=0.75,rely=0.888)

    # end of the creation of the buttons from a-z


    letter_click("*",letters_guessed)
    root.mainloop()
