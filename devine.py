import random

def devinez(x) :
    random_number = random.randint(1, x)
    devinez = 0
    while devinez != random_number:
         devinez = int(input(f"devinez un nombre entre un et {x}: "))
         if devinez < random_number:
            print("retentez votre chance. vous etes trop bas.")
         elif devinez > random_number:
            print("rentantez votre chance. vous etes trop haut")
    
    print("bravooo!! vous avez devine le bon nombre!")
    
devinez(50)