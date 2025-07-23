from ttkbootstrap import Window


class MainPanel(Window):
    def __init__(self):
        super().__init__(
            title="G-Numbers | Main Panel",
            themename="solar",
            size=(800, 600)
            )

        self.place_window_center()
