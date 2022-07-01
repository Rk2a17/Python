import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp == 'S':
        if you == 'W':
            return False
        elif you =='G':
            return True
    elif comp == 'W':
        if you == 'S':
            return True
        elif you =='G':
            return False
    elif comp == 'G':
        if you == 'S':
            return False
        elif you =='W':
            return True

print("Computer's Turn: Snake(S) Water(W) or Gun(G)")
randNo = random.randint(1,3)
# print(randNo)
if randNo==1:
    comp = 'S'
elif randNo==2:
    comp = 'W'
elif randNo ==3:
    comp = 'G'

# print("Computer's Turn: Snake(S) Water(W) or Gun(G)")
you = input("Player 2 Turn: Snake(S) Water(W) or Gun(G)")

a = gameWin(comp, you)

print(f"Computer Choose {comp}")
print(f"you Choose {you}")

if a == None:
    print("game is tie !")
elif a:
    print("you win")
else:
    print("you Loose")
