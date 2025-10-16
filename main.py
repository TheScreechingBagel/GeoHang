import game_logic as game
import tkinter as tk
from tkinter import ttk
import gui_logic as gui


def main():
    country: str = game.choose_random_country(game.load_countries("countries_en"))

    def notice(memo: str, field: str):
        if field == "lives":
            lives_display.set(memo)
        elif field == "word":
            word.set(memo)
        elif field == "status":
            status.set(memo)
        elif field == "guesses":
            guessed_sofar.set(memo)

    def key_handler(event: tk.Event):
        lives, guessed_letters, word_state = game.advance_game(
            event.char, lives_global.get(), guessed_letters_global.get(), country
        )
        notice("", "status")
        notice(guessed_letters, "guesses")
        notice(str(lives), "lives")
        notice(word_state, "word")

        if game.check_lose_condition(lives):
            notice("you lost", "status")
            notice(f"it was {country}...", "word")
        elif game.check_win_condition(country, guessed_letters):
            notice(country, "word")
            notice("you won!", "status")

        lives_global.set(lives)
        guessed_letters_global.set(guessed_letters)

    def report_callback_exception(self, exc, val, tb):
        notice(str(val), "status")

    tk.Tk.report_callback_exception = report_callback_exception

    root = tk.Tk()
    root.title("thegame")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=tk.NSEW)

    lives_display = tk.StringVar()
    word = tk.StringVar()
    status = tk.StringVar()
    guessed_sofar = tk.StringVar()

    ttk.Label(mainframe, textvariable=lives_display).grid(column=1, row=1, sticky=tk.EW)
    ttk.Label(mainframe, textvariable=word).grid(column=2, row=2, sticky=tk.EW)
    ttk.Label(mainframe, textvariable=status).grid(column=3, row=3, sticky=tk.EW)
    ttk.Label(mainframe, textvariable=guessed_sofar).grid(column=3, row=1, sticky=tk.EW)

    # root.columnconfigure(0, weight=1)
    # root.rowconfigure(0, weight=1)
    # mainframe.columnconfigure(2, weight=1)
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    guessed_letters_global = tk.StringVar()
    lives_global = tk.IntVar()
    lives_global.set(5)

    notice("0", "lives")

    notice(" ".join(game.display_word(country, "")), "word")

    root.bind("<Key>", key_handler)

    root.mainloop()


if __name__ == "__main__":
    main()
