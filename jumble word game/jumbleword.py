from random import sample
from getpass import getpass

author = 'Jencent Dizon'
link = 'https://github.com/I-am-Programmer-101'
print(f'Author: {author}\nLink: {link}\n')

def play():
    while True:
        input_word = getpass("Enter a word: ")
        print(sample(input_word, len(input_word)))
        input_again = input("Guess te word: ")
        if input_word == input_again:
            print("Ypu guess it")
        else:
            print("Better luck next time!")
            prompt = input("Do you want to play again? [y/n] ")
            if prompt == "y" or prompt == "Y":
                play()
            else:
                print("Run Again")
                break

if __name__ == "__main__":
    s = input("Press S or s to Start the game: ")
    if s == "s" or s == "S":
        play()
    else:
        print("Run Again")