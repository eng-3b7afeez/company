import ttkbootstrap as ttk
from ttkbootstrap.validation import (
    add_text_validation,
    add_phonenumber_validation,
    add_option_validation,
)
from ..utils import EntryLabelFrame


class CustomerUpdateForm(ttk.Frame):
    def __init__(self, parent, api, customer):
        super(CustomerUpdateForm, self).__init__(master=parent)
        self.api = api
        self.customer = customer
        self.initialize_vars()
        self.initialize_frames()
        self.layout()
        self.input_validation()

    def initialize_vars(self):
        self.name = ttk.StringVar(value=self.customer.name)
        self.mobile = ttk.StringVar(value=self.customer.mobile)
        self.mobile2 = ttk.StringVar(value=self.customer.mobile2)
        self.company = ttk.StringVar(value=self.customer.company)
        self.rating = ttk.IntVar(value=self.customer.rating)
        self.comment = ttk.StringVar(value=self.customer.comment)

    def initialize_frames(self):
        self.label_frame = ttk.LabelFrame(self, text="Update Customer")
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
            self.buttons_frame, text="Update", command=self.submit_data, width=20
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
        self.data = {
            "name": self.name.get(),
            "mobile": self.mobile.get(),
            "mobile2": self.mobile2.get(),
            "company": self.company.get(),
            "rating": int(self.rating.get()),
            "comment": self.comment.get(),
        }
        req = self.api.update(endpoint=f"customers/{self.customer.id}/", data=self.data)
        if req in range(300):
            self.cancel()

    def cancel(self):
        self.pack_forget()
        self.master.initialize_table()
