import ttkbootstrap as ttk
from ttkbootstrap.validation import (
    add_text_validation,
    add_phonenumber_validation,
    add_option_validation,
)
from ..utils import EntryLabelFrame
from ..logger import logger


class CustomerCreateForm(ttk.Frame):
    def __init__(self, parent, api):
        super(CustomerCreateForm, self).__init__(master=parent)
        self.api = api
        self.initialize_vars()
        self.initialize_frames()
        self.layout()
        self.input_validation()

    def initialize_vars(self):
        self.name = ttk.StringVar()
        self.mobile = ttk.StringVar()
        self.mobile2 = ttk.StringVar()
        self.company = ttk.StringVar()
        self.rating = ttk.IntVar(value=6)
        self.comment = ttk.StringVar()


    def initialize_frames(self):
        self.label_frame = ttk.LabelFrame(self, text="New Customer")
        self.name_frame = EntryLabelFrame(
            self.label_frame, text="Name", text_variable=self.name
        )
        self.mobile_frame = EntryLabelFrame(
            self.label_frame, text="Mobile", text_variable=self.mobile
        )
        self.mobile2_frame = EntryLabelFrame(
            self.label_frame, text="Mobile2", text_variable=self.mobile2
        )
        self.company_frame = EntryLabelFrame(
            self.label_frame, text="Company", text_variable=self.company
        )
        self.rating_frame = EntryLabelFrame(
            self.label_frame, text="Rating", text_variable=self.rating
        )
        self.comment_frame = EntryLabelFrame(
            self.label_frame, text="Comment", text_variable=self.comment
        )
        self.buttons_frame = ttk.Frame(self.label_frame)
        self.submit_button = ttk.Button(
            self.buttons_frame, text="Create", command=self.submit_data, width=20
        )
        self.cancel_button = ttk.Button(
            self.buttons_frame, text="Cancel", command=self.cancel, width=20
        )

    def layout(self):
        self.label_frame.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.9)
        self.submit_button.pack(side="left", anchor="w", padx=20)
        self.cancel_button.pack(side="right", anchor="e", padx=20)
        self.buttons_frame.pack(fill="x", pady=100)

    def input_validation(self):
        add_text_validation(self.name_frame.entry, when="focusout")
        add_phonenumber_validation(self.mobile_frame.entry, when="focusout")
        add_phonenumber_validation(self.mobile2_frame.entry, when="focusout")
        add_text_validation(self.company_frame.entry, when="focusout")
        add_option_validation(self.rating_frame.entry, [_ for _ in range(1, 11)])
        add_text_validation(self.comment_frame.entry, when="focusout")

    def submit_data(self):
        data = {
            "name": self.name.get(),
            "mobile": self.mobile.get(),
            "mobile2": self.mobile2.get(),
            "company": self.company.get(),
            "rating": int(self.rating.get()),
            "comment": self.comment.get(),
        }
        my_logger = logger("customer_create.log")
        try:
            req = self.api.post(endpoint="customers/", data=data)
            if req[0] in range(300):
                my_logger.info(f"customer : {self.name.get()} has been added to database")
                self.name.set("")
                self.mobile.set("")
                self.mobile2.set("")
                self.company.set("")
                self.rating.set(6)
                self.comment.set("")
                self.cancel()

        except Exception as e:
            my_logger.exception(f"something went wrong: {e}")

    def cancel(self):
        self.pack_forget()
        self.master.initialize_table()
