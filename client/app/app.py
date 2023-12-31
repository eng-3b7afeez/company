import ttkbootstrap as ttk
from client.components import Header, Footer, Side
from client.forms import Login


class App(ttk.Window):
    def __init__(
        self,
    ):
        super(App, self).__init__(title="Setalco")
        self.geometry(
            f"{self.winfo_screenwidth()}x{self.winfo_screenheight()-173}+-20+0"
        )
        self.username = ttk.StringVar(value="Guest")
        self.header = Header(self)
        self.side = Side(self)
        self.login = Login(self)
        self.footer = Footer(self)

        self.layout()

        self.bindings()
        self.style.theme_use("superhero")
        self.mainloop()

    def layout(self):
        self.header.place(relx=0.02, rely=0, relwidth=0.95, relheight=0.1)
        self.side.place(relx=0.02, rely=0.12, relwidth=0.2, relheight=0.76)
        self.login.place(relx=0.25, rely=0.12, relwidth=0.73, relheight=0.76)
        self.footer.place(relx=0.02, rely=0.88, relwidth=0.95, relheight=0.1)

    def bindings(self):
        self.bind("<Escape>", lambda _: self.quit())
