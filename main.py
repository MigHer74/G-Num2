from ui.main_panel import MainPanel
from src.tools import verify_database


if __name__ == "__main__":
    verify_database()

    app = MainPanel()
    app.mainloop()
