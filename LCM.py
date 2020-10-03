def findlcm(i,j) : #statement finding LCM
    prime = dict() #set prime to dict
    for x in range(i, j+1) : #statement looping for x in that range
        def findprime(x):  # statement find prime
            ans = dict() #set ans to dict
            a = 2 #set a value to 2
            while x != 1 and a ** 2 <= x: #looping while x is not 1 and a^2 is small than x
                num = 0 #set num value to zero
                while x % a == 0: #looping while x divided by a until zero
                    num += 1 #num = num + 1
                    x = x // a #x = x divide a
                if num > 0: #if num bigger than 0
                    ans[a] = num #set ans dict to num
                elif a == 2: #if a = 2
                    a += 1 #a = a + 1
                else: #if not above
                    a += 2 #a = a + 2
            if x != 1: #if x is not 1
                ans[x] = 1 #set ans dict to 1
            return ans #take ans value
        jwb = findprime(x) #set jwb value from findprime statement
        for key in jwb: #looping for key in jwb
            if not key in prime or prime[key] < jwb[key] : #if not key in prime or prime dict smaller than jwb dict
                prime[key] = jwb[key] #set prime dict = jwb dict
    jwb = 1 #set jwb value to 1
    for key in prime : #for key in prime
        jwb *= key ** prime[key] #jwb = jwb * key power prime
    return  jwb #take jwb value

i,j = map(int,input().split()) #input i and j
print(findlcm(i,j)) #printout the result
