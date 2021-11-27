from tkinter import *
from random import sample
from tkinter import messagebox

author = 'Jencent Dizon'
link = 'https://github.com/I-am-Programmer-101'
print(f'Author: {author}\nLink: {link}\n')

rt = Tk()
rt.title("Jumble Word")
rt.geometry("350x250")
rt.config(bg="lightblue")
rt.resizable(width=False, height=False)

# p1 = 0
# p2 = 0

# t = StringVar()

def CHECK():
    if entinput_player1.get() == entinput_player2.get():
        messagebox.showinfo("Correct", "Hooray you guess it!")
    else:
        messagebox.showwarning("Wrong", "Better luck next time!")

def GUESS_IT():
    word = sample(entinput_player1.get(), len(entinput_player1.get()))
    jumble_word = Label(rt, text=word, bg="lightblue", font="constantia 13 bold")
    jumble_word.place(x=155, y=50)

def RESET():
    entinput_player1.delete(0, END)
    entinput_player2.delete(0, END)

# all labels
lbltitle = Label(rt, text="Jumble Word", bg="lightblue", font="calibri 20 bold italic")
lblinput_player1 = Label(rt, text="Player 1 Word", bg="lightblue", font="calibri 12 italic")
lblinput_player2 = Label(rt, text="Player 2 Word", bg="lightblue", font="calibri 12 italic")
# lblplayer1_score = Label(rt, text=0, bg="lightblue", textvariable=t, font="calibri 10 bold")
# lblplayer2_score = Label(rt, text=0, bg="lightblue", textvariable=t, font="calibri 10 bold")

# all entries
entinput_player1 = Entry(rt, width=25, bg="lightblue", justify="center", show="*")
entinput_player2 = Entry(rt, width=25, bg="lightblue", justify="center")
# entp1_score = Entry(rt, width=5, bg="lightblue", font="calibri 12 bold", justify="center")
# entp2_score = Entry(rt, width=5, bg="lightblue", font="calibri 12 bold", justify="center")

# all buttons
btncheck = Button(rt, text="CHECK", bg="lightblue", fg="green", width=12, font="calibri 12 bold", command=CHECK)
btnguessnow = Button(rt, text="GUESS NOW", bg="lightblue", fg="green", width=12, font="calibri 12 bold", command=GUESS_IT)
btnreset = Button(rt, text="RESET", bg="lightblue", fg="green", width=12, font="calibri 12 bold", command=RESET)

# display labels on screen
lbltitle.place(x=100, y=5)
lblinput_player1.place(x=20, y=95)
lblinput_player2.place(x=20, y=147)
# lblplayer1_score.place(x=20, y=40)
# lblplayer2_score.place(x=62, y=40)

# display entry on screen
entinput_player1.place(x=125, y=100)
entinput_player2.place(x=125, y=150)
# entp1_score.place(x=5, y=60, height=17)
# entp2_score.place(x=50, y=60, height=17)

# display button on screen
btnguessnow.place(x=10, y=200)
btncheck.place(x=120, y=200)
btnreset.place(x=230, y=200)

rt.mainloop()