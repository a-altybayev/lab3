import random
def game():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    num = random.randint(1, 20)
    a = int(input("Take a guess.\n"))
    cnt = 0
    while True:
        cnt+=1
        if a<num:
            print("Your guess is too low")
        elif a>num:
            print("Your guess is too much")
        else:
            print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
            break
        a = int(input("Take a guess.\n"))
game()