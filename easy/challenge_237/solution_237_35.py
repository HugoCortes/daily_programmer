print ("\n*************************************************************\n")
print ("Daily Programming Challenge #237 [Easy] Broken Keyboard\n")
print ("Link: https://www.reddit.com/r/dailyprogrammer/comments/3pcb3i/20151019_challenge_237_easy_broken_keyboard/")
print ("\n*************************************************************\n")

inFile     = "input_1.in"
dictionary = "enable1.txt"

with open(inFile) as fileInput:
    readLines = int(fileInput.readline())
    try:
        for i, line in enumerate(fileInput):
            if i == readLines:
                break;
            possible = []
            line = line.strip("\n")
            for word in open(dictionary).read().split():
                if set(word).issubset(set(line)):
                    possible.append(word)
            print ("%s = %s" % (line, max(possible, key=len)))
    finally:
        fileInput.close()