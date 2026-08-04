#Checking whether a number is prime or not
num = int(input("Enter a number:"))  
def isPrime(num):
    if num <= 1:
        print("Not a prime")
    else:
        for i in range(2 , num ):
            if num % i == 0:
                print("Not a prime")

                break
                
        else:
            print("Prime Number")   
isPrime(num)
