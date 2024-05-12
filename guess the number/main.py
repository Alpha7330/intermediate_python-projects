import art
import random
print(art.logo)
print("welcome to the number guessing game!")
dif=input("choose difficulty e:easy and h:hard")

def hard():
  lives=5
  num=[]
  for i in range(1,101):
    num.append(i)
  op=random.choice(num)
  print("you have 5 attempts to guess")
  guess=int(input("make a guess:"))
  while lives!=0:
    if guess=="" or guess==" ":
      print("invalid input")
    elif guess==op:
      print(f"you got it! the answer was {op}")
      break
    elif guess>op:
      print("Too high")
      print("guess again")
      lives-=1
      if lives!=1:
        print(f"you have {lives} attempts remaining to guess the number")
        guess=int(input("make a guess:"))
      if lives==0:
        print(f"you lost the game,the number is {op}")
        break      
    elif guess<op:
      print("Too low")
      print("guess again")
      lives-=1
      if lives!=0:
        print(f"you have {lives} attempts remaining to guess the number")
        guess=int(input("make a guess:"))
      if lives==0:
        print(f"you lost the game,the number is {op}")
        break  
    else:
      break


def easy():
  num=[]
  lives=10
  for i in range(1,101):
    num.append(i)
  op=random.choice(num)
  print("you have 10 attempts to guess")
  guess=int(input("make a guess:"))
  while lives!=0:
    if guess=="" or guess==" ":
      print("invalid input")
    elif guess==op:
      print(f"you got it! the answer was {op}")
      break
    elif guess>op:
      print("Too high")
      print("guess again")
      lives=lives-1
      if lives!=0:
        print(f"you have {lives} attempts remaining to guess the number")
        guess=int(input("make a guess:"))
      if lives==0:
        print(f"you lost the game,the number is {op}")
        break   
    elif guess<op:
      print("Too low")
      print("guess again")
      lives-=1
      if lives!=0:
        print(f"you have {lives} attempts remaining to guess the number")
        guess=int(input("make a guess:"))
      if lives==0:
        print(f"you lost the game,the number is {op}")
        break   
    else:
      break
    
if dif=='e':
  easy()
elif dif=='h':
  hard()
else:
  print("invalid input")
  
   


