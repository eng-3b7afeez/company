import ttkbootstrap as ttk
from ttkbootstrap.validation import add_regex_validation
import jwt
from ..utils import EntryLabelFrame, Toaster
from ..api import Api
from ..pages import Main
from ..logger import logger


class Login(ttk.Frame):
    def __init__(self, parent):
        super(Login, self).__init__(master=parent)
        self.username = ttk.StringVar(value="")
        self.password = ttk.StringVar(value="")
        self.toaster = Toaster()
        self.initialize_children()
        self.layout()
        self.username_frame.entry.focus()
        self.initialize_validations()
        self.logger = logger("login.log")

    def initialize_children(self):
        self.main_frame = ttk.LabelFrame(self, text="Login")
        self.username_frame = EntryLabelFrame(
            self.main_frame, text="Username", text_variable=self.username
        )
        self.password_frame = EntryLabelFrame(
            self.main_frame, text="Password", text_variable=self.password, show="*"
        )
        self.buttons_frame = ttk.Frame(self.main_frame)
        self.login_button = ttk.Button(
            self.buttons_frame, text="Login", width=15, command=self.login
        )
        self.clear_button = ttk.Button(
            self.buttons_frame, text="Clear", width=15, command=self.clear
        )

    def layout(self):
        self.login_button.pack(side="left", anchor="w", padx=20)
        self.clear_button.pack(side="right", anchor="e", padx=20)
        self.buttons_frame.pack(fill="x", padx=20, pady=100)
        self.main_frame.place(
            relx=0.5, rely=0.5, relwidth=0.25, relheight=0.5, anchor="center"
        )

    def initialize_validations(self):
        add_regex_validation(
            self.username_frame.entry, r"^[a-zA-Z0-9]", when="focusout"
        )
        add_regex_validation(
            self.password_frame.entry, r"^[a-zA-Z0-9]", when="focusout"
        )

    def login(self):
        username = self.username.get()
        password = self.password.get()
        self.api = Api((username, password))
        try:
            req = self.api.post(
                endpoint="token/", data={"username": username, "password": password}
            )
            if (
                jwt.decode(req[1]["access"], options={"verify_signature": False})[
                    "username"
                ]
                == username
            ):
                self.master.username.set(value=username)
                self.master.main = Main(
                    self.master, api=self.api
                )
                self.master.main.place(
                    relx=0.25, rely=0.12, relwidth=0.73, relheight=0.76
                )
                self.logger.info(f"{self.username.get()} has logged in successfully")
                self.place_forget()
                self.toaster.toast(
                    title="Login success", message="you've logged in successfully"
                )
        except Exception as e:
            self.toaster.toast(title="Login problem", message=f"something went wrong while login : {e}")
            self.logger.exception(f"something went wrong: {e}")
    def clear(self):
        self.username.set(value="")
        self.password.set(value="")
