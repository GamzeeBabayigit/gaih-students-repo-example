

def prime_first(possiblePrime): 
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
                break
          
        if isPrime:
            print("Function First", possiblePrime)
                 
def prime_second(possiblePrime):
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            print("Function Second" ,possiblePrime)



for i in range(2,1000):
    if i<500:
        prime_first(i)
    else:
        prime_second(i)
