# ex175: # Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
# Examples:
# divisors(12) --> [2, 3, 4, 6]
# divisors(25) --> [5]
# divisors(13) --> "13 is prime"
def divisors(number):
    return [num for num in range(2, number) if number % num == 0] or f"{number} is prime"


if __name__ == "__main__":
    print(divisors(12))  # [2, 3, 4, 6]
    print(divisors(25))  # [5]
    print(divisors(13))  # 13 is prime
