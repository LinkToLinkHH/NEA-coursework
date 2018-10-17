import random
Lives = 2
password = "Lumagar"

while Lives != "0":
    print("Welcome to the music quiz!")
    player1 = input("What is your name?")
    player1pw = input("What is the password?")
    if player1pw == password:
        print("You can play the music quiz!!")

    else:
        print("You are not authorised to play this quiz!!")

    Songs = open("Songstxt")
    Songs = Songs.read()
    Artists = open("Artist.txt")
