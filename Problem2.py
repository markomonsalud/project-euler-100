import sys

def fiboEvenSum(number):
    total=0
    fiboNumber = 0
    prevFiboNumber = 1
    prevFiboNumber2 = 0 
    while (fiboNumber <= number):
        if(fiboNumber%2 == 0):
            total += fiboNumber
        
        fiboNumber = prevFiboNumber + prevFiboNumber2
        prevFiboNumber2 = prevFiboNumber
        prevFiboNumber = fiboNumber

    return total

def main():
    
    print(fiboEvenSum(sys.argv[1]))

if __name__ == "__main__":
    main()