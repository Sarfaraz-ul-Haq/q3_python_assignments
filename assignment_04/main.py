# function to check whether a given number is even or odd
def is_even_or_odd(num: int) -> str:
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


# function to check whether a given number is prime or not
def is_prime(num: int) -> bool:
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True


# declare variables
user_name: str
favorite_numbers: list[int] = []

# initialize variables after user input
user_name = input("Enter your name: ")
first_favorite_number: int = int(input("Enter your first favorite number: "))
second_favorite_number: int = int(input("Enter your second favorite number: "))
third_favorite_number: int = int(input("Enter your third favorite number: "))

# appending the user's favorite numbers to the "favorite_numbers" list
favorite_numbers.append(first_favorite_number)
favorite_numbers.append(second_favorite_number)
favorite_numbers.append(third_favorite_number)

# ___________________________________________________________________

print(f"\nHello, {user_name}! Let's explore your favorite numbers:\n")

# ___________________________________________________________________

for number in favorite_numbers:
    print(f"The number {number} is {is_even_or_odd(number)}.")

print("\n")  # line break

for number in favorite_numbers:
    print(f"The number {number} and it's square: {number, number ** 2}")
# ___________________________________________________________________

print(f"\nAmazing! The sum of your favorite numbers is: {sum(favorite_numbers)}")

# ___________________________________________________________________

if is_prime(sum(favorite_numbers)):
    print(f"Wow, {sum(favorite_numbers)} is a prime number")
else:
    print(f"{sum(favorite_numbers)} is not a prime number")
