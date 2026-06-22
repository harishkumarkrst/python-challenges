import random


def generate_secret_number(min_val, max_val):
    """
    Return a random integer between min_val and max_val.
    """
    return random.randint(min_val, max_val)


def check_guess(secret, guess):
    """
    Compare guess with secret number.
    """
    if guess < secret:
        return "too_low"
    elif guess > secret:
        return "too_high"
    else:
        return "correct"


def play_round(secret, guess, attempts):
    """
    Process one round of guessing game.
    """
    result = check_guess(secret, guess)

    return {
        "guess": guess,
        "result": result,
        "attempts": attempts,
        "game_over": result == "correct"
    }


def calculate_score(attempts, max_attempts):
    """
    Calculate score from 0 to 100.
    """
    remaining = max_attempts - attempts
    score = int(100 * remaining / (max_attempts - 1))

    return max(0, score)