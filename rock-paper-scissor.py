import random
game=['rock','paper','scissor']
p1=random.choice(game)
print("party 1:",p1)
p2=random.choice(game)
print("party 2:",p2)
if p1=='rock' and p2=='scissor':
    print("p1 won the task")
elif p1=='paper' and p2=='rock':
    print("p1 won the task")
elif p1=='scissor' and p2=='paper':
    print("p1 won the task")
else:
    print("p2 won the task")
