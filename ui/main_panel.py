from ttkbootstrap import Window, Frame, Labelframe, Radiobutton, Entry, Label
from ttkbootstrap import Button, StringVar
from src.engine import game_engine
import src.db_tools as db


class MainPanel(Window):
    def __init__(self):
        super().__init__(
            title="G-Numbers | Main Panel",
            themename="solar",
            size=(555, 560),
            resizable=(False, False)
            )

        self.option = StringVar(value=None)
        self.game = StringVar(value=None)

        self.place_window_center()
        self.select_game()
        self.select_type()
        self.panel_short_game()
        self.panel_long_game()
        self.panel_buttons()
        self.panel_results()
        self.load_data()
        self.initial_state()

    def select_game(self):
        self.fr_select_game = Labelframe(self, text=" Select Game ",
                                         labelanchor="n")
        self.fr_select_game.grid(row=0, column=0, padx=15, pady=15,
                                 sticky="nswe")

        self.radio_play = Radiobutton(self.fr_select_game, text="Play",
                                      value="play", variable=self.option,
                                      command=self.select_play)
        self.radio_play.grid(row=0, column=0, padx=(20, 20), pady=(15, 0),
                             sticky="w")

        self.radio_replay = Radiobutton(self.fr_select_game, text="RePlay",
                                        value="replay", variable=self.option,
                                        command=self.select_replay)
        self.radio_replay.grid(row=1, column=0, padx=(20, 20), pady=(15, 15),
                               sticky="w")

    def select_type(self):
        self.fr_select_type = Labelframe(self, text=" Select Game Type ",
                                         labelanchor="n")
        self.fr_select_type.grid(row=1, column=0, padx=15, pady=15, sticky="n")

        self.radio_short = Radiobutton(self.fr_select_type, text="Short Game",
                                       value="short", variable=self.game,
                                       command=self.select_short)
        self.radio_short.grid(row=0, column=0, padx=(20, 20), pady=(15, 0),
                              sticky="w")

        self.radio_long = Radiobutton(self.fr_select_type, text="Long Game",
                                      value="long", variable=self.game,
                                      command=self.select_long)
        self.radio_long.grid(row=1, column=0, padx=(20, 20), pady=(15, 15),
                             sticky="w")

    def panel_short_game(self):
        self.fr_short_game = Labelframe(self,
                                        text=" Last Result of The Short Game ",
                                        labelanchor="n")
        self.fr_short_game.grid(row=0, column=1, padx=(15, 15), pady=(15, 15),
                                sticky="n")

        self.label_short_01 = Label(self.fr_short_game, text="Game #1")
        self.label_short_01.grid(row=0, column=0, padx=(15, 0), pady=(15, 15))

        self.entry_item_01 = Entry(self.fr_short_game, width=3,
                                   justify="center")
        self.entry_item_01.grid(row=0, column=1, padx=(15, 0), pady=(15, 15))

        self.entry_item_02 = Entry(self.fr_short_game, width=3,
                                   justify="center")
        self.entry_item_02.grid(row=0, column=2, padx=(15, 0), pady=(15, 15))

        self.entry_item_03 = Entry(self.fr_short_game, width=3,
                                   justify="center")
        self.entry_item_03.grid(row=0, column=3, padx=(15, 0), pady=(15, 15))

        self.entry_item_04 = Entry(self.fr_short_game, width=3,
                                   justify="center")
        self.entry_item_04.grid(row=0, column=4, padx=(15, 0), pady=(15, 15))

        self.entry_item_05 = Entry(self.fr_short_game, width=3,
                                   justify="center")
        self.entry_item_05.grid(row=0, column=5, padx=(15, 0), pady=(15, 15))

        self.entry_item_06 = Entry(self.fr_short_game, width=3,
                                   justify="center")
        self.entry_item_06.grid(row=0, column=6, padx=(15, 15), pady=(15, 15))

    def panel_long_game(self):
        self.fr_long_game = Labelframe(self,
                                       text=" Last Result of The Long Game ",
                                       labelanchor="n")
        self.fr_long_game.grid(row=1, column=1, padx=(15, 15), pady=(15, 15),
                               sticky="n")

        self.label_long_01 = Label(self.fr_long_game, text="Game #1")
        self.label_long_01.grid(row=0, column=0, padx=(15, 0), pady=(15, 15))

        self.entry_item_11 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_11.grid(row=0, column=1, padx=(15, 0), pady=(15, 15))

        self.entry_item_12 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_12.grid(row=0, column=2, padx=(15, 0), pady=(15, 15))

        self.entry_item_13 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_13.grid(row=0, column=3, padx=(15, 0), pady=(15, 15))

        self.entry_item_14 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_14.grid(row=0, column=4, padx=(15, 0), pady=(15, 15))

        self.entry_item_15 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_15.grid(row=0, column=5, padx=(15, 0), pady=(15, 15))

        self.entry_item_16 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_16.grid(row=0, column=6, padx=(15, 15), pady=(15, 15))

        self.label_long_02 = Label(self.fr_long_game, text="Game #2")
        self.label_long_02.grid(row=1, column=0, padx=(15, 0), pady=(15, 15))

        self.entry_item_21 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_21.grid(row=1, column=1, padx=(15, 0), pady=(15, 15))

        self.entry_item_22 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_22.grid(row=1, column=2, padx=(15, 0), pady=(15, 15))

        self.entry_item_23 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_23.grid(row=1, column=3, padx=(15, 0), pady=(15, 15))

        self.entry_item_24 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_24.grid(row=1, column=4, padx=(15, 0), pady=(15, 15))

        self.entry_item_25 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_25.grid(row=1, column=5, padx=(15, 0), pady=(15, 15))

        self.entry_item_26 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_26.grid(row=1, column=6, padx=(15, 15), pady=(15, 15))

        self.label_long_03 = Label(self.fr_long_game, text="Game #3")
        self.label_long_03.grid(row=2, column=0, padx=(15, 0), pady=(15, 15))

        self.entry_item_31 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_31.grid(row=2, column=1, padx=(15, 0), pady=(15, 15))

        self.entry_item_32 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_32.grid(row=2, column=2, padx=(15, 0), pady=(15, 15))

        self.entry_item_33 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_33.grid(row=2, column=3, padx=(15, 0), pady=(15, 15))

        self.entry_item_34 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_34.grid(row=2, column=4, padx=(15, 0), pady=(15, 15))

        self.entry_item_35 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_35.grid(row=2, column=5, padx=(15, 0), pady=(15, 15))

        self.entry_item_36 = Entry(self.fr_long_game, width=3,
                                   justify="center")
        self.entry_item_36.grid(row=2, column=6, padx=(15, 15), pady=(15, 15))

    def panel_results(self):
        self.fr_results = Labelframe(self, width=368, height=180,
                                     text=" Game Results ", labelanchor="n")
        self.fr_results.grid(row=2, column=1, padx=(15, 15),
                             pady=(15, 15), sticky="n")
        self.fr_results.grid_propagate(True)

    def panel_buttons(self):
        self.fr_buttons = Frame(self)
        self.fr_buttons.grid(row=2, column=0, padx=(15, 15), pady=(15, 15))

        self.button_play = Button(self.fr_buttons, width=15, text="Play Game",
                                  command=self.press_play)
        self.button_play.grid(row=0, column=0)

        self.button_cancel = Button(self.fr_buttons, width=15,
                                    text="Reset Game", command=self.load_data)
        self.button_cancel.grid(row=1, column=0, pady=(15, 0))

        self.button_previous = Button(self.fr_buttons, width=15,
                                      text="Previous Results")
        self.button_previous.grid(row=2, column=0, pady=(15, 0))

        self.button_close = Button(self.fr_buttons, width=15, text="Close App",
                                   command=self.destroy)
        self.button_close.grid(row=3, column=0, pady=(15, 0))

    def build_results(self, game_type: str) -> list:
        (label_results_01, label_results_02, label_results_03,
         label_results_04, label_results_f) = game_engine(game_type)

        if game_type == "short":
            row_result_1 = f"5+ --> {", ".join(label_results_01)}"
            row_result_2 = f"4 ---> {", ".join(label_results_02)}"
            row_result_3 = f"3 ---> {", ".join(label_results_03)}"
            row_result_4 = f"2 ---> {", ".join(label_results_04)}"
            row_result_f = f"Final: {", ".join(label_results_f)}"
        else:
            row_result_1 = f"6+ --> {", ".join(label_results_01)}"
            row_result_2 = f"5 ---> {", ".join(label_results_02)}"
            row_result_3 = f"4 ---> {", ".join(label_results_03)}"
            row_result_4 = f"3 ---> {", ".join(label_results_04)}"
            row_result_f = f"Final: {", ".join(label_results_f)}"

        Label(self.fr_results, text=row_result_1).grid(row=0, column=0,
                                                       padx=(15, 15),
                                                       pady=(10, 0),
                                                       sticky="w")
        Label(self.fr_results, text=row_result_2).grid(row=1, column=0,
                                                       padx=(15, 15),
                                                       pady=(10, 0),
                                                       sticky="w")
        Label(self.fr_results, text=row_result_3).grid(row=2, column=0,
                                                       padx=(15, 15),
                                                       pady=(10, 0),
                                                       sticky="w")
        Label(self.fr_results, text=row_result_4).grid(row=3, column=0,
                                                       padx=(15, 15),
                                                       pady=(10, 0),
                                                       sticky="w")
        Label(self.fr_results, text=row_result_f).grid(row=4, column=0,
                                                       padx=(15, 15),
                                                       pady=(10, 10),
                                                       sticky="w")

    def load_data(self):
        self.short_data, self.long_data = db.get_latest_data()

        self.state_entries(True)
        self.clear_entries("both")

        if self.short_data:
            self.fill_entries("short")
        if self.long_data:
            self.fill_entries("long")

        self.state_entries(False)
        self.initial_state()

    def state_entries(self, enable=True, section="both"):
        if section == "short" or section == "both":
            for widget in self.fr_short_game.winfo_children():
                if isinstance(widget, Entry):
                    widget.config(state='normal' if enable else 'disabled')
        if section == "long" or section == "both":
            for widget in self.fr_long_game.winfo_children():
                if isinstance(widget, Entry):
                    widget.config(state='normal' if enable else 'disabled')

    def clear_entries(self, section="both"):
        if section == "short" or section == "both":
            for entry in self.fr_short_game.winfo_children():
                if isinstance(entry, Entry):
                    entry.delete(0, 'end')
        if section == "long" or section == "both":
            for entry in self.fr_long_game.winfo_children():
                if isinstance(entry, Entry):
                    entry.delete(0, 'end')

    def clear_results(self):
        for widget in self.fr_results.winfo_children():
            if isinstance(widget, Label):
                widget.destroy()

    def initial_state(self):
        self.option.set(None)
        self.game.set(None)
        self.radio_play.config(state="normal")
        self.radio_replay.config(state="normal")
        self.radio_short.config(state="disabled")
        self.radio_long.config(state="disabled")
        self.button_play.config(state="disabled")
        self.button_cancel.config(state="disabled")
        self.button_previous.config(state="normal")

    def fill_entries(self, type_game):
        if type_game == "short":
            entries = self.fr_short_game.winfo_children()
            for i, entry in enumerate(entries):
                if isinstance(entry, Entry):
                    entry.delete(0, 'end')
                    entry.insert(0, self.short_data[i + 2])
        else:
            row = 0
            item = 0
            entries = self.fr_long_game.winfo_children()
            for entry in entries:
                if isinstance(entry, Entry):
                    if item <= 5:
                        entry.delete(0, 'end')
                        entry.insert(0, self.long_data[row][item + 3])
                        item += 1
                    else:
                        row += 1
                        item = 0
                        entry.delete(0, 'end')
                        entry.insert(0, self.long_data[row][item + 3])
                        item += 1

    def select_play(self):
        self.radio_play.config(state="disabled")
        self.radio_replay.config(state="disabled")
        self.radio_short.config(state="normal")
        self.radio_long.config(state="normal")
        self.button_previous.config(state="disabled")
        self.button_cancel.config(state="normal")
        self.clear_results()

    def select_replay(self):
        self.radio_play.config(state="disabled")
        self.radio_replay.config(state="disabled")
        self.radio_short.config(state="normal")
        self.radio_long.config(state="normal")
        self.button_previous.config(state="disabled")
        self.button_cancel.config(state="normal")
        self.clear_results()

    def select_short(self):
        if self.option.get() == "play":
            self.game_selected = "short"
            self.state_entries(True, "short")
            self.radio_short.config(state="disabled")
            self.radio_long.config(state="disabled")
            self.button_play.config(state="normal")
            self.button_cancel.config(state="normal")
            self.entry_item_01.focus()
        else:
            self.build_results("short")

    def select_long(self):
        if self.option.get() == "play":
            self.game_selected = "long"
            self.state_entries(True, "long")
            self.radio_short.config(state="disabled")
            self.radio_long.config(state="disabled")
            self.button_play.config(state="normal")
            self.button_cancel.config(state="normal")
            self.entry_item_11.focus()
        else:
            self.build_results("long")

    def press_play(self):
        if self.game_selected == "short":
            db.update_games("short")

            entries = self.fr_short_game.winfo_children()
            numbers = [int(entry.get()) for entry in entries
                       if isinstance(entry, Entry)]

            numbers.insert(0, "S")
            numbers.insert(1, "W1")
            numbers.insert(2, 1)

            numbers = tuple(numbers)

            db.insert_values(numbers)

            self.build_results("short")
        else:
            db.update_games("long")

            entries = self.fr_long_game.winfo_children()
            numbers = [int(entry.get()) for entry in entries
                       if isinstance(entry, Entry)]

            numbers_final = []
            number = 0

            for i in range(3):
                numbers_final.insert(0, "L")
                numbers_final.insert(1, "W1")
                numbers_final.insert(2, i + 1)

                for item in range(number, len(numbers)):
                    if item > number + 5:
                        break
                    else:
                        numbers_final.append(numbers[item])

                db.insert_values(tuple(numbers_final))
                numbers_final = []
                number += 6

            self.build_results("long")

        self.load_data()
