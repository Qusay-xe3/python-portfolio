#pin_space_table.py

GUESSES_PER_SECOND = 10

for pin in range (4, 8 + 1):
    guesses = 10 ** pin
    guesses_per_seconds = guesses // GUESSES_PER_SECOND
    guess_per_minute = guesses_per_seconds // 60
    days = guess_per_minute // (60 * 24)
    print(f"{pin} digits: {guesses} PINs, {guess_per_minute} minutes, {days} days")