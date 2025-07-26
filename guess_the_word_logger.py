secret = "python"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    try:
        guess = input("Guess the word: ").strip()

        if not guess.isalpha():
            raise ValueError("Invalid input: only letters allowed")

        if guess.lower() == secret:
            print("Yes! You guessed it!")
            break
        else:
            print("No! Try again!")

    except Exception as e:
        print("Something went wrong:", e)
        with open("log.txt", "a") as log_file:
            log_file.write(str(e) + "\n")

    finally:
        attempts += 1
        print(f"Attempt {attempts}/{max_attempts}\n")

else:
    print("Game over! The secret word was:", secret)
