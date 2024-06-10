#For example, ,
#and the sum of the digits in the number is.
#Find the sum of the digits in the number 

def factorial(n):
    if n == 0:
        return(1)
    elif n == 1:
        return(1)
    else:
        return(n*factorial(n-1))
    
def main():
    x = 6 #Numero deseado para resolver
    answer = factorial(x)
    digits = list(str(answer))
    sumDIgit = 0
    for digit in digits:
        sumDIgit += int(digit)
    print(sumDIgit)

main()
