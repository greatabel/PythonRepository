CENTS_PER_TOONIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUATER = 25
CENTS_PER_DIME   = 10
CENTS_PER_NICKEL = 5

cents = int(input("Enter the number of cents:?"))

print(" ", cents // CENTS_PER_TOONIE , "toonies")
cents = cents % CENTS_PER_TOONIE

print(" ", cents // CENTS_PER_LOONIE , "loonies")
cents = cents % CENTS_PER_LOONIE

print(" ", cents // CENTS_PER_QUATER , "quaters")
cents = cents % CENTS_PER_QUATER

print(" ", cents // CENTS_PER_DIME , "dimes")
cents = cents % CENTS_PER_DIME

print(" ", cents // CENTS_PER_NICKEL , "nickels")
cents = cents % CENTS_PER_NICKEL

print(" ", cents, "penies")




