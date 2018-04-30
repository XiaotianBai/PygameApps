import random


list = [i for i in range(9)]
list = list + list
random.shuffle(list)

print(list)

