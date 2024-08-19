import random
#basic variables
deck = []
suits=["\u2660","\u2663","\u2666","\u2665"]
values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
playerHand = []
dealerHand = []
playerValue = 0
dealerValue = 0
playerDone = False
playerWon = False
burnt = []
#evaluate function for getting value of card
def eval(card,handValue):
    if(card[1:]=="J" or card[1:]=="Q" or card[1:]=="K"):
        return 10
    if(card[1:] == "A" and handValue <= 10 ):
        return 11
    if(card[1:] == "A" and handValue > 10):
        return 1
    else:
        return int(card[1:])
#creation of deck
for s in suits:
    for v in values:
        deck.append(s+v)
#deck test
#print("\n")
#for cards in deck:
    #print(cards+"\n")
#beginning hands
for x in range(2):
    pCard = random.randint(0,51)
    playerHand.append(deck[pCard])
for x in range(2):
    dCard = random.randint(0,51)
    dealerHand.append(deck[dCard])
#establishing starting hand values
playerValue+=(eval(playerHand[0],playerValue)+eval(playerHand[1],playerValue))
dealerValue+=(eval(dealerHand[0],dealerValue)+eval(dealerHand[1],dealerValue))
#telling player their hand and visible dealers card
print("Your cards are " + playerHand[0] + " & " + playerHand[1])
print("\n The dealers hand is " + dealerHand[0])
#checking for blackjack off deal
if(playerValue==21):
    print("BlackJack nice hand!")
    playerDone=True
    exit
if(dealerValue==21):
    print("Dealer has BlackJack, better luck next time!")
    playerDone=True
    exit
#main game loop
while(playerDone==False):
    choice = input("\nWould you like to hit or stand :: H or S?\n")
    if(choice == "S"):
        playerDone==True
        break
    if(choice == "H"):
        playerHand.append(deck[random.randint(0,51)])
        playerValue+=eval(playerHand[len(playerHand)-1],playerValue)
        print(playerHand)
    if(playerValue == 21):
        playerDone = True
        break
    if(playerValue > 21):
        if (playerHand[len(playerHand)-1][1:] == "A"):
            playerValue-=10
        else:
            playerDone = True
            break
    if(playerValue < 21):
        continue
#dealer play
print(dealerHand)
while(dealerValue<21):
    if(dealerValue >= 17):
        break
    if(dealerValue < 17):
        dealerHand.append(deck[random.randint(0,51)])
        dealerValue+=eval(dealerHand[len(dealerHand)-1],dealerValue)
        print(dealerHand[len(dealerHand)-1])
    if(dealerValue > 21):
        if (dealerHand[len(dealerHand)-1][1:] == "A"):
            dealerValue-=10
        else:
            playerDone = True
            break
#handle win cons
if(playerValue > 21):
    print("You bust!")
if((playerValue > dealerValue) and playerValue <= 21):
    print("You won, good hand!")
if((playerValue < dealerValue) and dealerValue <= 21):
    print("Dealer wins, nice try")
if((playerValue < dealerValue) and dealerValue > 21):
    print("Dealer Bust! You win!")
