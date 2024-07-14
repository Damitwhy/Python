import random

# print(f'A random float between 0 & 1.0: {random.random()}')
print(f'A random int between 0 & 10: {random.randrange(11)}')
print('A random choice from a list: ' + random.choice(['paper', 'scissors', 'rock']))
deck = ['hearts', 'diamonds', 'spades', 'clubs']
random.shuffle(deck)
print(deck)