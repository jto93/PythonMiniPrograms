#This program takes a statement and translates it to Pig Latin

def convertWord(ans): 
    
    vow = ['a','e','i','o','u','y','A','E','I','O','U','Y']
    
    x = len(ans)
    y = 0
    pre = ""
    post = ""
    a = True

    while x > 0: 
        while a == True:         
            if ans[y] in vow: 
                pre += (ans[y:])
                a = False

            if ans[y] not in vow: 
                post += (ans[y])
                
            y += 1
            x = x - 1
        x = 0

    #add "ay" to the end of the post
    if len(post) > 0: 
        post += ('a')
        post += ('y')

    elif len(post) == 0: 
        post += ('y')
        post += ('a')
        post += ('y')

    return(pre + post)

def swineTalk(): 
    ans = input('What statement would you like translated to Pig Latin? ')
    words = ans.split(' ')
    j = len(words)
    i = 0
    statement = ''
    
    while i < j: 
        conWord = convertWord(words[i])
        if i+1 < j: 
            statement += conWord + ' '
        elif i+1 == j:
            statement += conWord + ' is your statement in Pig Latin'
            print(statement)
            break
            
        i += 1
 


swineTalk()