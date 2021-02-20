import random 

randNum=random.randint(1,1000)
primes = []
def primeNum(possiblePrime): 
        randNum=random.randint(1,1000)
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                return primeNum(randNum+1)
            else:
                return possiblePrime

R = int(3) 
C = int(3) 

matrix = [] 
  
for i in range(R):		  
	a =[] 
	for j in range(C):	 

          a.append(int(primeNum(randNum))) 
	matrix.append(a) 

# For printing the matrix 
for i in range(R): 
	for j in range(C): 
		print( matrix[i][j])
         
	print("\n") 

            

