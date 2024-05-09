import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Call clear_console() whenever you want to clear the console

import art
print(art.logo)
auc={}
choice="yes"
def bid_wl():
    name=input("enter your name\n")
    bid=int(input("enter your bid\n"))
    auc[name]=bid
    clear_console()
    print("Are there any other bidders\n")
    choice=input("enter yes or no\n").lower()

    if choice=="yes":
       bid_wl()
    elif choice=="no":
       pass
    else:
       pass
def highest_bidder():
  highest_bid=0
  winner=None
  for bidder in auc:
    if auc[bidder]>highest_bid:
      highest_bid=auc[bidder]
      winner=bidder
  print(f"The winner in auction is {winner} with ${auc[winner]}")    
bid_wl()  
highest_bidder()

