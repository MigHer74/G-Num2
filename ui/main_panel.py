from ttkbootstrap import Window, Frame, Labelframe, Radiobutton, Entry, Label
from ttkbootstrap import Button, StringVar


class MainPanel(Window):
    def __init__(self):
        super().__init__(
            title="G-Numbers | Main Panel",
            themename="solar",
            size=(555, 580),
            resizable=(False, False)
            )

        self.place_window_center()
        self.select_game()
        self.select_type()
        self.panel_short_game()
        self.panel_long_game()
        self.panel_buttons()
        self.panel_results()

    def select_game(self):
        self.fr_select_game = Labelframe(self, text=" Select Game ",
                                         labelanchor="n")
        self.fr_select_game.grid(row=0, column=0, padx=15, pady=15,
                                 sticky="nswe")

        self.radio_play = Radiobutton(self.fr_select_game, text="Play",
                                      value="play")
        self.radio_play.grid(row=0, column=0, padx=(20, 20), pady=(15, 0),
                             sticky="w")

        self.radio_replay = Radiobutton(self.fr_select_game, text="RePlay",
                                        value="replay")
        self.radio_replay.grid(row=1, column=0, padx=(20, 20), pady=(15, 15),
                               sticky="w")

    def select_type(self):
        self.fr_select_type = Labelframe(self, text=" Select Game Type ",
                                         labelanchor="n")
        self.fr_select_type.grid(row=1, column=0, padx=15, pady=15, sticky="n")

        self.radio_short = Radiobutton(self.fr_select_type, text="Short Game",
                                       value="short")
        self.radio_short.grid(row=0, column=0, padx=(20, 20), pady=(15, 0),
                              sticky="w")

        self.radio_long = Radiobutton(self.fr_select_type, text="Long Game",
                                      value="long")
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
        self.fr_results = Labelframe(self, width=368, height=200,
                                     text=" Game Results ", labelanchor="n")
        self.fr_results.grid(row=2, column=1, padx=(15, 15),
                             pady=(15, 15), sticky="n")
        self.fr_results.grid_propagate(True)

    def panel_buttons(self):
        self.fr_buttons = Frame(self)
        self.fr_buttons.grid(row=2, column=0, padx=(15, 15), pady=(15, 15))

        self.button_play = Button(self.fr_buttons, width=15, text="Play Game")
        self.button_play.grid(row=0, column=0)

        self.button_cancel = Button(self.fr_buttons, width=15,
                                    text="Reset Game")
        self.button_cancel.grid(row=1, column=0, pady=(15, 0))

        self.button_cancel = Button(self.fr_buttons, width=15, text="New Game")
        self.button_cancel.grid(row=2, column=0, pady=(15, 0))

        self.button_close = Button(self.fr_buttons, width=15, text="Close App")
        self.button_close.grid(row=3, column=0, pady=(15, 0))
