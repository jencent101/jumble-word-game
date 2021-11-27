from random import sample, choice
from emoji import emojize

author = 'Jencent Dizon'
link = 'https://github.com/I-am-Programmer-101'
print(f'Author: {author}\nLink: {link}\n')

score = 0
print(f"Your score is {score}")

word_lst = [
'apple','banana','grapes','lemonade','dalandan',
'jeepny','tricycle','owner','train','truck',
'penguin','snake','jaguar','parrot','giraffe',
'cancer','local','broom','grass','leopard',
'hammer','ginger','rocket', 'kangaroo', 'mystical',
'chamber', 'lacoste', 'emerald', 'kingdom', 'princess',
'hebreo', 'lucas', 'victory', 'carol', 'human', 'ranger',
]

while True:
    cw = choice(word_lst)
    rw = sample(cw, len(cw))
    print(rw)
    user = input("Guess it : ")
    if user == cw:
        score += 1
        print(emojize("🎊Congratulations🎊"))
    else:
        print(emojize("😝It's a wrong answer😝"))
        prompt = input("Press C to continue and press any button to exit")
        if prompt == "c" or prompt == "C":
            user
        else:
            print("Better luck next time!")
            print(f"You have a {score} total scores")
            break