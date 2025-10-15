from game_logic import *


def main():
    country = choose_random_country(load_countries("countries_en"))
    guessed_letters: list[str] = []
    lives = 5

    while True:
        print(f"Lives: {lives}")
        print(*display_word(country, guessed_letters))

        guess = get_player_guess(guessed_letters)
        if check_guess(guess, country):
            guessed_letters.append(guess)
        else:
            lives = update_lives(lives, False)

        if check_lose_condition(lives):
            print("you lost")
            print(f"it was {country}...")
            break
        elif check_win_condition(country, guessed_letters):
            print(f"it was {country}!")
            print("you won!")
            break


if __name__ == "__main__":
    main()
