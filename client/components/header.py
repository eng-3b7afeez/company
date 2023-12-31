import ttkbootstrap as ttk
from ..app.settings import FONT, LARGE_FONT


class Header(ttk.Frame):
    def __init__(self, master):
        super(Header, self).__init__(master=master)

        self.theme = ttk.StringVar(value="superhero")

        self.logo = ttk.Label(
            self,
            text="Setalco",
            font=f"{FONT} {LARGE_FONT}",
            background="red",
        )
        self.logo.pack(side="left", padx=10)
        self.settings = ttk.Spinbox(
            self,
            textvariable=self.theme,
            values=self.master.style.theme_names(),
            command=lambda: self.master.style.theme_use(self.theme.get()),
        )
        self.settings.pack(side="right", padx=10)
        self.account_label = ttk.Label(self, textvariable=self.master.username)
        self.account_label.pack(side="right", padx=50)
