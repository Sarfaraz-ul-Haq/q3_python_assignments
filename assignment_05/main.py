import random


def main() -> None:
    print("Welcome to the High-Low Game!")
    print("-----------------------------\n")

    NUM_ROUNDS: int = int(
        input("How many rounds do you want to play? Enter a number: ")
    )

    round: int = 1
    score: int = 0

    for i in range(NUM_ROUNDS):
        print(f"\n🔴 ROUND {round}\n")

        computer_number: int = random.randint(1, 100)
        user_number: int = random.randint(1, 100)

        print(f"Your number is {user_number}\n")

        user_guess: str = input(
            "Do you think your number is higher or lower than the computer's?  "
        )

        higher_and_correct = (
            user_number > computer_number and user_guess.lower() == "higher"
        )

        lower_and_correct = (
            user_number < computer_number and user_guess.lower() == "lower"
        )

        if higher_and_correct or lower_and_correct:
            score += 1
            print(f"\nYou were right! The computer's number was {computer_number}")
            print(f"Your score is now {score}")
            print("--------------------------------------------")
        else:
            print(f"\nThats incorrect! The computer's number was {computer_number}")
            print(f"Your score is {score}")
            print("--------------------------------------------")

        round += 1

    if score == NUM_ROUNDS:
        print(f"🎊🎊🎊 Wow! You won all {NUM_ROUNDS} rounds. Perfect score!")
    elif score > NUM_ROUNDS / 2:
        print(f"🎊 Great job! You won {score} out of {NUM_ROUNDS} rounds.")
    elif score == NUM_ROUNDS / 2:
        print(f"You won {score} out of {NUM_ROUNDS} rounds. Exactly half!")
    elif score == NUM_ROUNDS / 3:
        print(f"You won {score} out of {NUM_ROUNDS} rounds. You hit the 1/3 mark!")
    else:
        print(f"You won {score} out of {NUM_ROUNDS} rounds. Better luck next time!")


if __name__ == "__main__":
    main()
