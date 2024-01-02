from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.validation import (
    add_text_validation,
    add_phonenumber_validation,
    add_option_validation,
)
from ..utils import EntryLabelFrame, ComboLabelFrame, CheckboxLabelFrame
from ..logger import logger

class OperationUpdateForm(ttk.Frame):
    def __init__(self, parent, api, operation):
        super(OperationUpdateForm, self).__init__(master=parent)
        self.api = api
        self.operation = operation
        self.initialize_vars()
        self.initialize_frames()
        self.layout()
        self.input_validation()

    def initialize_vars(self):
        self.customer = ttk.StringVar(value=self.operation.customer)
        self.material = ttk.StringVar(value=self.operation.material)
        self.material_from_storage = ttk.BooleanVar(value=self.operation.material_from_storage)
        self.height = ttk.DoubleVar(value=self.operation.height)
        self.width = ttk.DoubleVar(value=self.operation.width)
        self.thickness = ttk.DoubleVar(value=self.operation.thickness)
        self.work_duration = ttk.IntVar(value=self.operation.work_duration)
        self.amount = ttk.DoubleVar(value=self.operation.amount)
        self.laser_cut = ttk.BooleanVar(value=self.operation.laser_cut)
        self.is_active = ttk.BooleanVar(value=self.operation.is_active)
        self.file_path=ttk.StringVar(value=self.operation.file_path)
        self.customers = self.api.get(endpoint="customers/")[1]

    def initialize_frames(self):
        self.label_frame = ttk.LabelFrame(self, text="Update Operation")
        self.customer_frame = ComboLabelFrame(
            self.label_frame, text_variable=self.customer, values=[customer["name"] for customer in self.customers]
        )
        self.material_frame = ComboLabelFrame(
            self.label_frame, text_variable=self.material, values=["ST", "SUS", "AL", "BR",]
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
        self.file_button_frame = ttk.Frame(self.label_frame)
        self.file_button = ttk.Button(self.file_button_frame, text="open file", command=self.open_file)
        self.buttons_frame = ttk.Frame(self.label_frame)
        self.submit_button = ttk.Button(
            self.buttons_frame, text="Update", command=self.submit_data, width=20
        )
        self.cancel_button = ttk.Button(
            self.buttons_frame, text="Cancel", command=self.cancel, width=20
        )

    def layout(self):
        self.label_frame.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.9)
        self.file_button.pack()
        self.file_button_frame.pack(fill="x", pady=20)
        self.submit_button.pack(side="left", anchor="w", padx=20)
        self.cancel_button.pack(side="right", anchor="e", padx=20)
        self.buttons_frame.pack(fill="x", pady=50)

    def input_validation(self):
        pass

    def open_file(self):
        file_path = filedialog.askopenfile(initialdir="E:/WORK SETALCO")
        self.file_path.set(value=file_path.name)

    def get_customer_id(self):
        for customer in self.customers:
            if customer.get("name") == self.customer.get():
                return customer.get("id")

    def submit_data(self):
        data = {
            "material": self.material.get(),
            "material_from_storage": self.material_from_storage.get(),
            "width": self.width.get(),
            "height": self.height.get(),
            "thickness": self.thickness.get(),
            "work_duration": self.work_duration.get(),
            "amount": self.amount.get(),
            "laser_cut": self.laser_cut.get(),
            "is_active": self.is_active.get(),
            "file_path": self.file_path.get(),
            "customer": self.get_customer_id()
        }
        my_logger = logger('operation_update.log')
        try:
            req = self.api.update(endpoint=f"operations/{self.operation.id}/", data=data)
            if req in range(300):
                my_logger.info(f"operation updated successfully for customer {self.customer.get()} by user: {self.api.auth[0]}")
                self.cancel()
        except Exception as e:
            my_logger.exception(f"something went wrong: {e}")

    def cancel(self):
        self.pack_forget()
        self.master.initialize_table()

