print ("\n*************************************************************\n")
print ("Daily Programming Challenge #236 [Easy] Random Bag System\n")
print ("Link: https://www.reddit.com/r/dailyprogrammer/comments/3ofsyb/20151012_challenge_236_easy_random_bag_system/")
print ("\n*************************************************************\n")

import random

def TetrisBag(pieces):
    string = []
    while len(string) < 50:
        random.shuffle(pieces)
        string += pieces[:]
    return ''.join(string[:50])
    
def TetrisValidate(bag, size):
    for i in range(0, len(bag), size):
        try:
            result = len(set(bag[i:i+size])) == len(bag[i:i+size])
        except:
            result = len(set(bag[i:len(bag)])) == len(bag[i:len(bag)])
    return result
    
pieces = ['O', 'I', 'S', 'Z', 'L', 'J', 'T']
bag = TetrisBag(pieces)
print (bag)
print (TetrisValidate(bag, len(pieces)))
