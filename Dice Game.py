print('''                                                THE DICE GAME
                                    (GET READY FOR SOME BETTING! AND EARN CASH$$$) ''')
import random
a = input("Player 1-Enter your nickname:")
b = input("Player 2-Enter your nickname:")
a_score=0
b_score=0
for i in range(10):
    a_value = random.randint(1,6)
    b_value = random.randint(1,6)
    print(a," rolled:",a_value)
    print(b," rolled:",b_value)
    if a_value>b_value:
        print(a," wins")
        a_score +=1
    elif a_value<b_value:
        print(b," wins")
        b_score += 1
    else:
        print('Scores level')
    input("Press enter to continue:")
print(a,' final score',a_score)
print(b,' final score',b_score)
diff_1 = a_score - b_score
diff_2 = b_score - a_score
if a_score>b_score:
    print(a," won the game by",diff_1,"points $$$")
elif a_score<b_score:
    print(b," won the game by",diff_2,"points $$$")
else:
    print("Match tied")
