import random

tries= 0
lower_bound = 1
upper_bound = 100
trials = int(input("How many trials do you need to guess the correct number :)"))

correct_guess = random.randint(lower_bound, upper_bound)



for attempt in range(trials):
    tries = attempt++1
    guess = int(input(f"Please enter your guess between 1 and {upper_bound} :"))
    if guess < correct_guess:
        if tries < trials:
            print(f"{guess} is too low!")
        else:
            print(f" No attempts left, {trials} trials as chosen have been exhausted")
    
    elif guess > correct_guess:
         if tries < trials:
            print(f"{guess} is to high!")
         else:
            print(f" No attempts left, {trials} trials as chosen have been exhausted")
    
    else:
        print(f"Congratulation! {guess} is the right guess! with {tries} tries out of {trials}")
        break
