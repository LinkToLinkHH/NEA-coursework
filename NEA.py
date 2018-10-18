import random
Lives = 2
password = "Lumagar"

print("Welcome to the music quiz!")
player = input("What is your name?")
playerpw = input("What is the password?")
if playerpw == password:
    print("You can play the music quiz!!")

else:
    print("You are not authorised to play this quiz!!")


def remove():
    test = items[i].replace("A","-")

    test0 = test.replace("E","-")

    test1 = test0.replace("I","-")
        
    test2 = test1.replace("O","-")

    test3 = test2.replace("U","-")
    print(test3)
def choose_songs():
    Songs = open("Songs.txt""r")
    Songs = Songs.read()
    Artists = open("Artists.txt""r")
    items = Songs.split(',')
    i = random.randint(0,2)
    remove()
    Artists = Artists.read()
    items = Artists.split(',')
    remove()

    print("Let's start!!")
    choose_song()
    
