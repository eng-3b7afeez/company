import ttkbootstrap as ttk
from ..utils import Toaster
from ..forms import CustomerCreateForm, CustomerUpdateForm
from ..components.table import DataTable
from ..data import Customer


class Customers(ttk.Frame):
    def __init__(self, parent, api):
        super(Customers, self).__init__(master=parent)
        self.api = api
        self.toaster = Toaster()
        self.initialize_table()
        self.add_customer_form = CustomerCreateForm(
            self, api=self.api
        )

    def initialize_table(self):
        self.all_customers = self.api.get(endpoint="customers/")[1]
        self.buttons_frame = ttk.Frame(self)
        self.add_customer_button = ttk.Button(
            self.buttons_frame, text="Add Customer", command=lambda: self.add_customer()
        )
        self.add_customer_button.pack(side="right")
        self.buttons_frame.pack(fill="x")
        self.coldata = [
            {"text": "id"},
            {"text": "Name", "stretch": True},
            {"text": "Mobile1", "stretch": True},
            {"text": "Mobile2", "stretch": True},
            {"text": "Company", "stretch": True},
            {"text": "rating", "stretch": True},
            {"text": "comment", "stretch": True},
        ]
        self.rowdata = []
        try:
            self.rowdata = [customer.values() for customer in self.all_customers]
        except Exception as e:
            self.toaster.toast("Customer data problem", f"something went wrong with: {e}")
        self.table = DataTable(self, coldata=self.coldata, rowdata=self.rowdata)
        self.table.view.bind("<Delete>", self.delete_customer)
        self.table.view.bind("<Double-1>", self.update_customer)
        self.table.pack(fill="both", expand=True, padx=10, pady=10)

    def add_customer(self):
        self.table.pack_forget()
        self.buttons_frame.pack_forget()
        self.add_customer_form.pack(fill="both", expand=True, padx=10, pady=10)

    def update_customer(self, _):
        selected_row = self.table.get_rows(selected=True)[0]
        customer = Customer(*selected_row.values)
        self.table.pack_forget()
        self.buttons_frame.pack_forget()
        self.update_customer_form = CustomerUpdateForm(self, api=self.api, customer=customer)
        self.update_customer_form.pack(fill="both", expand=True, padx=10, pady=10)
    def delete_customer(self, _):
        selected_customer = self.table.get_rows(selected=True)[0]
        customer_id = selected_customer.values[0]
        answer = self.toaster.yes_no_box(parent=self, title="Delete Customer", message=f"Are you sure you want delete Customer: {selected_customer.values[1]}")

        if answer == "Yes":
            selected_customer.delete()
            self.api.delete(endpoint=f"customers/{customer_id}/")
