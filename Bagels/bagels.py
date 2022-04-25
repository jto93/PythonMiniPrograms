#Bagels from Al Sweigart's Big Book of Python
from random import randint

def generateNumber(num): 
    ans = ''
    for i in range(num): 
        ans += str((randint(1,9)))
    return ans

def checkGuess(uInput, ans):
    if len(uInput) > 3:
        return 'String is too long'
    if uInput == ans: 
        return 'You got it right!'

    clues = []

    for i in range(len(uInput)):
        if uInput[i] == ans[i]:
            clues.append('Fermi')
        elif uInput[i] in ans: 
            clues.append('Pico')
    
    if len(clues) == 0: 
        return 'Bagels'
    else: 
        clues.sort()
        return ' '.join(clues)

def main():
    numDigits = 3
    maxGuesses = 10
    
    print('I am thinking of a 3 digit number. Try to guess what it is.\nHere are some clues:\n')
    print('When I Say:\tThat Means:\n  Pico\t\tOne digit is correct but in the wrong position.\n')
    print('  Fermi\t  One digit is correct and in the right position.\n')
    print('  Bagels\t No digit is correct.\n')
    while True: 
        ans = generateNumber(numDigits)
        guess = 0        
        print('I have thought up a number.\n')

        while guess <= maxGuesses: 
            print('You have %s guesses left' %(maxGuesses - guess))
            uInput = input('Guess #%s: ' %(guess+1))
            outcome = checkGuess(uInput, ans)
            print(outcome)
            

            if outcome == 'You got it right!': 
                break

            guess += 1  
            if guess == maxGuesses: 
                print('You ran out of guesses.')
                print('The correct answer was %s' %(ans))
                break
        
        q = input('Do you want to play again? (yes or no)')
        q = q.lower()
        if not q.startswith('y'):
            break
    print('Thanks for playing!')



main()