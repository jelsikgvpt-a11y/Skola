#vytvor mi niaku jednoduch hru v pythone
import random   
def guess_the_number():
    number_to_guess = random.randint(1, 1001)
    attempts = 0
    max_attempts = 20

    print("Welcome to 'Guess the Number'!")
    print("I have selected a number between 1 and 1000.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
if __name__ == "__main__":
    guess_the_number()

