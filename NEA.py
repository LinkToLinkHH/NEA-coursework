import random
Lives = 2
password = "Lumagar"

print("Welcome to the music quiz!")
player = str(input("What is your name?"))
playerpw = str(input("What is the password?"))
if playerpw == password:
    print("You can play the music quiz!!")

else:
    print("You are not authorised to play this quiz!!")

correctanswer = True
def correct():
    if correctanswer == True:
        points = points +3

def incorrect():
    correctanswer = False
    if correctanswer == False:
        Lives = Lives - 1

    def lives():
        if lives == 2:
            points = points + 3
        elif lives == 1:
            points = points + 1

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
    if Songs != Songs:
        correct() or incorrect()

    
    print("Let's start!!")
    choose_song()


if Lives == 0:
    print("You have no more lives left!")
    Player = open("Players.txt" "a")
    Player = Players.txt.append(player)


    
