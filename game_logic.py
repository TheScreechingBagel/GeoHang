import random
import util
import gui_logic as gui


# Core Game Functions
def load_countries(filename: str) -> list[str]:
    """Load countries from file and return as a list"""
    with open(filename, "r") as countries_file:
        countries_list = []
        for i in countries_file:
            countries_list.append(i.strip())
        return countries_list


def choose_random_country(countries_list: list[str]) -> str:
    """Select and return a random country"""
    return util.remove_accents(
        countries_list[random.randint(0, len(countries_list) - 1)]
    )  # TODO: make readable:tm:


def display_word(country: str, guessed_letters: list[str]) -> list[str]:
    """Display the current state of the word with revealed letters"""
    hidden_word: list[str] = []
    for i in country:
        if i in guessed_letters or i.lower() in guessed_letters:
            hidden_word.append(i)
        elif i in [" ", "'", "-"]:
            hidden_word.append(i)
        else:
            hidden_word.append("_")
    return hidden_word


def get_player_guess(guessed_letters: list[str]) -> str:
    """Get and validate player's letter guess"""
    while True:
        given_letter = gui.key_handler()
        if given_letter.isalpha() and len(given_letter) == 1:
            if given_letter in guessed_letters:
                gui.notice("you already tried that one, do another")
            else:
                break
        else:
            gui.notice("i don't think that's a letter, try again")
    return given_letter.lower()


def check_guess(letter: str, country: str) -> bool:
    """Check if the guessed letter is in the country name"""
    if letter in country or letter.upper() in country:
        return True
    else:
        return False


def update_lives(lives: int, is_correct: bool) -> int:
    """Update and return remaining lives"""
    if is_correct:
        return lives
    else:
        return lives - 1


def check_win_condition(country: str, guessed_letters: list[str]) -> bool:
    """Check if player has won the game"""
    guessed_letters += [" ", "'", "-"]
    win_statement = False
    for i in country:
        if i.lower() in guessed_letters:
            win_statement = True
        else:
            win_statement = False
            break
    return win_statement


def check_lose_condition(lives: int) -> bool:
    """Check if player has lost the game"""
    if lives == 0:
        return True
    else:
        return False


# Logging Functions
def log_game_result(country: str, result, attempts: int, guessed_letters: list[str]):
    """Save game result to log file"""
    pass


# Extra Feature Functions
def get_hint(country: str):
    """Provide a hint about the country's region"""
    pass
