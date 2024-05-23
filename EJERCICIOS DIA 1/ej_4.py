from random import randint

def guess():
    x = randint(1, 10)
    
    while True:
        attempt = input("Intenta adivinar el número entre 1 y 10: ")

        attempt = int(attempt)
        
        if attempt < x:
            print("Demasiado bajo")
        elif attempt > x:
            print("Demasiado alto")
        else:
            print("Adivinaste el número!")
            break
guess()
