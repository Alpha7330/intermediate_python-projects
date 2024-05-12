from art import logo
import os
import random
def clear():
  os.system('cls')
def deal_card():
  """returns a random card from deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card
def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
def compare(user_score,computer_score):
  if user_score>21 and computer_score>21:
    return "You went over. You lose"
  elif user_score==computer_score:
    return "it's a draw"
  elif computer_score==0:
    return "you lose, opponent has blackjack"
  elif user_score==0:
    return "you win, you have blackjack"
  elif user_score>21:
    return "you lose, you went over"
  elif computer_score>21:
    return "you win, opponent went over"
  elif user_score>computer_score:
    return "you win"
  else:
    return "you lose"  
    
      

def play_game():
  print(logo)
  user_cards=[]
  computer_cards=[]
  is_game_over=False
  for _ in range(2):
   user_cards.append(deal_card())
   computer_cards.append(deal_card())
  
  while not is_game_over:
    
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"yours cards are {user_cards} and your score is {user_score}")
    print(f"computer's first card is {computer_cards[0]}")
    if user_score==0 or computer_score==0 or user_score>21:
      is_game_over=True
    else:
      next_turn=input("do you want to draw another card? type 'y' or 'n'")
      if next_turn=='y':
        user_cards.append(deal_card())
      else:
        is_game_over=True
    
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
    
  print(f"your final hand is {user_cards} and your final score is {user_score}")
  print(f"computer's final hand is {computer_cards} and computer's final score is {computer_score}")
  print(compare(user_score,computer_score))
while input("do you want to play again? type 'y' or 'n'").lower()=='y':
  clear()
  play_game()
