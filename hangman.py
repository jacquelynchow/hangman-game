# import the random module
import random

# create our list of possible words and figure out what the word will be
wordList = ['apple', 'banana', 'kiwi']
word = random.choice(wordList)
# set the number of guesses along with a counter to keep track
total_guesses = len(word) + 5
counter = 0

# make a list the length of the word and insert that many Falses
boolList = []
for letter in word:
    boolList.append(False)
    # print out blank character spaces for each character in the word 
    # end keeps the letters on one line
    print(" _ ", end = '')

# while there is still guesses left, continue 
while counter <= total_guesses:
    # print the number of guesses left
    print("\nYou have " + str(total_guesses - counter) + " guesses left.")
    # check if you ran out of guesses  
    if counter == total_guesses:
        print("\nYou lost. :( The word was " + word + "! Try again :D\n")
        break
    # get user's guess
    guess = input("\nGuess a letter: ")
    # add one to counter 
    counter += 1
    # create index for boolList
    index = 0
    # loop through all the characters in the word 
    for letter in word:
        # check if any of the characters match your guess 
        if guess == letter:
            # set boollist at that index to True 
            boolList[index] = True
        # move to next character
        index += 1
    # loop through boolList, if True at that index, then reveal that letter 
    for i in range(len(boolList)):
        if boolList[i] == True:
            print(" " + word[i] + " ", end = '')
        # if the boolean is False, do not show that letter
        else:
            print(" _ ", end = '')

    # if there are no Falses left in the list, you know you're done!
    if False not in boolList:
        print("\n\nYou got the word. End of game!\n")
        break 

