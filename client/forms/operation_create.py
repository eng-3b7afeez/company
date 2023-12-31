import ttkbootstrap as ttk
from ttkbootstrap.validation import (
    add_text_validation,
    add_phonenumber_validation,
    add_option_validation,
)
from ..utils import EntryLabelFrame, ComboLabelFrame, CheckboxLabelFrame


class OperationCreateForm(ttk.Frame):
    def __init__(self, parent, api):
        super(OperationCreateForm, self).__init__(master=parent)
        self.api = api
        self.initialize_vars()
        self.initialize_frames()
        self.layout()
        self.input_validation()

    def initialize_vars(self):
        self.customer = ttk.StringVar(value="Customer")
        self.material = ttk.StringVar(value="Material")
        self.material_from_storage = ttk.BooleanVar(value=True)
        self.height = ttk.DoubleVar(value=0.0)
        self.width = ttk.DoubleVar(value=0.0)
        self.thickness = ttk.DoubleVar(value=0.0)
        self.work_duration = ttk.IntVar(value=0)
        self.amount = ttk.DoubleVar(value=0.0)
        self.laser_cut = ttk.BooleanVar(value=True)
        self.is_active = ttk.BooleanVar(value=True)
        self.customers = self.api.get(endpoint="customers/")[1]

    def initialize_frames(self):
        self.label_frame = ttk.LabelFrame(self, text="New Operation")
        self.customer_frame = ComboLabelFrame(
            self.label_frame, text_varialble=self.customer, values=[customer["name"] for customer in self.customers]
        )
        self.material_frame = ComboLabelFrame(
            self.label_frame, text_varialble=self.material, values=["ST", "SUS", "AL", "BR",]
        )
        self.material_from_storage_frame = CheckboxLabelFrame(
            self.label_frame, text="Material From Store", variable=self.material_from_storage
        )
        self.height_frame = EntryLabelFrame(
            self.label_frame, text="Height", text_variable=self.height
        )
        self.width_frame = EntryLabelFrame(
            self.label_frame, text="Width", text_variable=self.width
        )
        self.thickness_frame = EntryLabelFrame(
            self.label_frame, text="Thickness", text_variable=self.thickness
        )
        self.work_duration_frame = EntryLabelFrame(
            self.label_frame, text="Cutting Time", text_variable=self.work_duration
        )
        self.amount_frame = EntryLabelFrame(
            self.label_frame, text="Cost", text_variable=self.amount
        )
        self.is_active_frame = CheckboxLabelFrame(
            self.label_frame, text="Under Process", variable=self.is_active
        )
        self.laser_cut_frame = CheckboxLabelFrame(
            self.label_frame, text="Laser Machine", variable=self.laser_cut
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
        self.buttons_frame.pack(fill="x", pady=50)

    def input_validation(self):
        pass

    def get_customer_id(self):
        for customer in self.customers:
            if customer.get("name") == self.customer.get():
                return customer.get("id")

    def get_user_id(self):
        users = self.api.get(endpoint="users/")[1]
        for user in users:
            if user.get("username") == self.api.auth[0]:
                return user.get("id")

    def submit_data(self):
        self.data = {
            "material": self.material.get(),
            "material_from_storage": self.material_from_storage.get(),
            "width": self.width.get(),
            "height": self.height.get(),
            "thickness": self.thickness.get(),
            "work_duration": self.work_duration.get(),
            "amount": self.amount.get(),
            "laser_cut": self.laser_cut.get(),
            "is_active": self.is_active.get(),
            "user": self.get_user_id(),
            "customer": self.get_customer_id()
        }
        req = self.api.post(endpoint="operations/", data=self.data)
        if req[0] in range(300):
            self.cancel()

    def cancel(self):
        self.pack_forget()
        self.master.initialize_table()

