from ttkbootstrap import Window, Labelframe, Radiobutton
from ttkbootstrap import StringVar


class MainPanel(Window):
    def __init__(self):
        super().__init__(
            title="G-Numbers | Main Panel",
            themename="solar",
            size=(800, 600)
            )

        self.place_window_center()
        self.select_game()
        self.select_type()

    def select_game(self):
        self.fr_select_game = Labelframe(self, text="Select Game",
                                         labelanchor="n")
        self.fr_select_game.grid(row=0, column=0, padx=15, pady=15)

        self.radio_play = Radiobutton(self.fr_select_game, text="Play",
                                      value="play")
        self.radio_play.grid(row=0, column=0, padx=(20, 20), pady=(15, 0),
                             sticky="w")

        self.radio_replay = Radiobutton(self.fr_select_game, text="RePlay",
                                        value="replay")
        self.radio_replay.grid(row=1, column=0, padx=(20, 20), pady=(15, 15),
                               sticky="w")

    def select_type(self):
        self.fr_select_type = Labelframe(self, text="Select Game Type",
                                         labelanchor="n")
        self.fr_select_type.grid(row=1, column=0, padx=15, pady=15)

        self.radio_short = Radiobutton(self.fr_select_type, text="Short Game",
                                       value="short")
        self.radio_short.grid(row=0, column=0, padx=(20, 20), pady=(15, 0),
                              sticky="w")

        self.radio_long = Radiobutton(self.fr_select_type, text="Long Game",
                                      value="long")
        self.radio_long.grid(row=1, column=0, padx=(20, 20), pady=(15, 15),
                             sticky="w")
