#Counts the number of words in an inputted string

def countWords(): 
    ans = input('Enter a string to count the words: ')
    arr = ans.split(' ')
    print('Words: %i' %(len(arr)))
    
countWords()