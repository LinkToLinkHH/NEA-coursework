import random
import time

def undicided ( p1_wins, p2_wins):
    while p1_wins == p2_wins:
      roll0 = random.randint(1,6)
      roll1 = random.randint(1,6)
      if roll0 > roll1:
         print("P1 wins!")
         p1_wins = p1_wins +1

      elif roll0 == roll1:
         undicided( p1_wins, p2_wins)

      else:
         print("P2 Wins!")
         p2_wins = p2_wins +1

p1_wins = 0

p2_wins = 0

for x in range(1,5):
   p1_dice = random.randint(1,6)
   p1_2_dice = random.randint(1,6)

   p2_dice = random.randint(1,6)
   p2_2_dice = random.randint(1,6)

   p1_total = p1_dice + p1_2_dice
   p2_total = p2_dice + p2_2_dice

   print("Player 1 rolls...")
   #time.sleep(2)
   print("Player 1 rolls a total of:",p1_total)

   if (p1_total % 2) == 0:
      print("It's even! Add 10 points!")
      p1_total2 = p1_total + 10
   else:
      print("It's odd! Subtract 5 points!")
      p1_total2 = p1_total - 5

   #time.sleep(1)

   print("Player 2 rolls...")
   #time.sleep(2)
   print("Player 2 rolls a total of:",p2_total)

   if (p2_total % 2) == 0:
      print("It's even! Add 10 points!")
      p2_total2 = p2_total + 10
   else:
      print("It's odd! Subtract 5 points!")
      p2_total2 = p2_total - 5

      
   print(p1_total2)
   print(p2_total2)

   if p1_total2 < 0:
      p1_total2 = 0

   elif p2_total2 < 0:
      p2_total2 = 0


   if p1_total2 > p2_total2:
      print("P1 wins!")
      p1_wins = p1_wins + 1

   elif p1_total2 == p2_total2:
      print("It's a draw!")

   else:
      print("P2 wins!")
      p2_wins = p2_wins + 1 

   print("")
   
print(p1_wins)
print(p2_wins)

if p1_wins > p2_wins:
   print("P1 wins the game!")

elif p1_wins == p2_wins:
   print("Roll one dice to decide!")
   undicided( p1_wins, p2_wins)
  

else:
   print("P2 wins the gane!")
