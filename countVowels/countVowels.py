
def countVowels(): 
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    y = 0
    sum = 0
    count = 0
    
    strVow = ['a','e','i','o','u','y']
    sp = ' '
    
    ans = input('Enter a string to count vowels: ')
    ans = ans.lower()


    for x in ans: 
        
        if x == (strVow[0]):
            a += 1
        elif x == (strVow[1]):
            e += 1
        elif x == (strVow[2]):
            i += 1
        elif x == (strVow[3]):
            o += 1
        elif x == (strVow[4]):
            u += 1
        elif x == (strVow[5]):
            if ans[count-1] != ' ':
                y += 1
                
        count += 1

    vow = [a,e,i,o,u,y]
    i = 0
    while i < 6: 
        print('%s: %i' %(strVow[i], vow[i]))
        sum += vow[i]
        i += 1

    print('The statement has ' + str(sum) + ' vowels.')

countVowels()