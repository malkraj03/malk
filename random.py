import random
car=['sandra','tavera','scarpio']
print(car)
print("pick one:")
b=input()
a=random.choice(car)
print("random item from list is: ", a)
if(a==b):
    print("you won the game......")
else:
    print("you loss the game......")
