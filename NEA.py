#imports the random library
import random
#this lets the user have two lives
#before the person cannot play anymore
Lives = 2
#makes the password "Lumagar"
password = "Lumagar"
#starts the points off with 0
points = 0

print("Welcome to the music quiz!")
#Asks the user for their name
player = input("What is your name?")
#Asks the user for the password to play the quiz
playerpw = input("What is the password?")
#If the password equals to the password they can play
if playerpw == password:
    print("You can play the music quiz!!")


    #if the players lives get to "0" the players "name" and "points" is
    #put into the file as a leaderboard
    if Lives == 0:
        file = file.open("Players.txt","a")
        file.write(player)
        file.write(points)
        print(Players.txt)

        #this means that id correct is equal to True
    #the points would add on to the players score
    def correct():
        correct = True
        if correct == True:
            points()

    #this means that if correct is False
    #the lives would so down by one
    def incorrect():
        correct = False
        if correct == False:
            lives = lives - 1
    
        def points():
            if lives == 2:
                points = points + 1
            elif lives == 1:
                points = points + 1
    
        #opens the Songs file, reads it and splits the items(songs)
        def choose_songs():
            #opens the songs.txt file
            Songs = open("Songs.txt")
            #reads the file 
            Songs = Songs.read()
            #opens the artists file 
            Artists = open("Artists.txt")
            #splits the songs with a ","
            items = Songs.split(',')
            #this chooses the songs at random
            i = random.randint(0,2)
            #runs the remove function and removes "A,E,I,O,U"
            remove()
            #reads the Artists.txt file
            Artists = Artists.read()
            #splits the artist items(artist names)
            items = Artists.split(',')
            #removes "A,E,I,O,U" in their names
            remove()

        #replaces "A,E,I,O,U" from both the artists file
        #and the song file with "-" 
        def remove():
            test = items.replace("A","-")

            test0 = test.replace("E","-")
    
            test1 = test0.replace("I","-")
        
            test2 = test1.replace("O","-")

            test3 = test2.replace("U","-")
    

        print("Let's do this!!")
        #runs the code and chooses a song
        choose_songs()
        print(choose_songs)

    #if it does not equal to password then the player cannot play
else:
    print("You are not authorised to play this quiz!!") 
