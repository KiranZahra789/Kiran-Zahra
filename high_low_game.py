
print("Welcome to the high- low game")

import random
NUM_ROUNDS = 5
score = 0

for round in range (1 , NUM_ROUNDS + 1):
    print(f"Round {round}")

    player_num = random.randint(1,100)
    computer_num = random.randint(1,100)

    print(f"Your number is {player_num}")
    
    guess = input(("Do you think your number is higher or lower than the computer's?" ))

    if guess == "higher" and player_num > computer_num:
        print ("you were right! The computer number was",computer_num)
        score += 1
    elif guess == "lower" and player_num < computer_num:
        print ("You were right! The computer number was",computer_num)
        score +=1
    else:
        print("Awww'thats incorrect")

    print(f"The computer number was {computer_num}")
    
    print(f"your score is now {score}")
    
            

print("thanks for playing")

if score == NUM_ROUNDS:
    print("Congratulations! you won all rounds")
elif score > NUM_ROUNDS //2:
    print("Good! You played very well")
else:
    print(" you can do better next time")
