import ttkbootstrap as ttk
from ..app.settings import FONT, MEDIUM_FONT


class Footer(ttk.Frame):
    def __init__(self, master):
        super(Footer, self).__init__(master=master)
        self.copy_right = ttk.Label(
            self, text="@3b7afeez", font=f"{FONT} {MEDIUM_FONT}"
        )
        self.pack(side="bottom")
