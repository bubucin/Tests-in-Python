import random as r

def guess():
    random_num = r.randint(1,20)
    tries = 0
    while True:
        if tries == 0:
            print("Guess a number between one and twenty")
        tries += 1
        choice = int(input("->"))
        if choice < random_num:
            print("Too small")
        elif choice > random_num:
            print("Too big")
        elif choice == random_num:
            print(f"You guessed the number in {tries} tries")
            break

if __name__ == "__main__":
    guess()