#Checks if a string is a Palindrome

def checkIfPalindrome(): 
    var = "%"
    orAns = input("What string would you like to check for a palindrome? ")
    ans = orAns.replace(" ", "")
    ans = ans.replace(',',"")
    ans = ans.replace('.',"")
    ans = ans.replace('!','')
    ans = ans.replace('?','')
    ans = ans.replace('-','')
    
    ans = ans.lower()

    revAns = ans[::-1]

    if revAns == ans: 
        print("Nice, %s is a palindrome." %(orAns))

    else: 
        x = len(revAns)-1
        y = 0
        while x >= 0:
            print(revAns[x]) 
            if revAns[x] == ans[x]: 
                print('Match')
                y += 1
                
            x -= 1
        
        pct = (y / len(revAns)) * 100
        pct = format(pct,'.2f')
        
        print("Sorry, %s is not a palindrome. It is about %s%s palindrome." %(orAns, pct, var))

checkIfPalindrome()