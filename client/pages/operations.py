import ttkbootstrap as ttk
from ..utils import Toaster
from ..forms import OperationCreateForm, OperationUpdateForm
from ..components.table import DataTable
from ..data import Operation


class Operations(ttk.Frame):
    def __init__(self, parent, api):
        super(Operations, self).__init__(master=parent)
        self.api = api
        self.toaster = Toaster()
        self.initialize_table()

    def get_customer_name(self, id):
        customers = self.api.get(endpoint="customers/")[1]
        for customer in customers:
            if customer.get("id") == id:
                return customer.get("name")

    def get_user_username(self, id):
        users = self.api.get(endpoint="users/")[1]
        for user in users:
            if user.get("id") == id:
                return user.get("username")

    def initialize_table(self):
        self.buttons_frame = ttk.Frame(self)
        self.add_operation_button = ttk.Button(
            self.buttons_frame,
            text="Add Operation",
            command=self.add_operation,
        )
        self.add_operation_button.pack(side="right")
        self.buttons_frame.pack(fill="x")
        col_data = [
            {"text": "ID"},
            {"text": "Customer", "stretch": True},
            {"text": "User", "stretch": True},
            {"text": "Material", "stretch": True},
            {"text": "Material_from_storage", "stretch": True},
            {"text": "Width", "stretch": True},
            {"text": "Height", "stretch": True},
            {"text": "Thickness", "stretch": True},
            {"text": "Work_duration", "stretch": True},
            {"text": "Amount", "stretch": True},
            {"text": "Laser_cut", "stretch": True},
            {"text": "Is_active", "stretch": True},
            {"text": "file_path", "stretch": True},
            {"text": "date", "stretch": True},
        ]
        row_data = []
        try:
            data = self.api.get(endpoint="operations/")[1]
            for operation in data:
                row_data.append(
                    (
                        operation["id"],
                        self.get_customer_name(operation["customer"]),
                        self.get_user_username(operation["user"]),
                        operation["material"],
                        operation["material_from_storage"],
                        operation["width"],
                        operation["height"],
                        operation["thickness"],
                        operation["work_duration"],
                        operation["amount"],
                        operation["laser_cut"],
                        operation["is_active"],
                        operation["file_path"],
                        operation["date"],
                    )
                )
        except Exception as e:
            self.toaster.toast(title="something went wrong", message=f"something went wrong with: {e}")
        self.table = DataTable(self,  coldata=col_data, rowdata=row_data)
        self.table.view.bind("<Delete>", self.delete_operation)
        self.table.view.bind("<Double-1>", self.update_operation)
        self.table.pack(fill="both", expand=True, padx=10, pady=10)

    def add_operation(self):
        self.table.pack_forget()
        self.buttons_frame.pack_forget()
        self.add_operation_form = OperationCreateForm(
            self, api=self.api
        )
        self.add_operation_form.pack(fill="both", expand=True, padx=10, pady=10)

    def update_operation(self, _):
        selected_row = self.table.get_rows(selected=True)[0]
        operation = Operation(*selected_row.values)
        self.table.pack_forget()
        self.buttons_frame.pack_forget()
        self.update_operation_form = OperationUpdateForm(
            self, api=self.api, operation=operation
        )
        self.update_operation_form.pack(fill="both", expand=True, padx=10, pady=10)

    def delete_operation(self, _):
        selected_operation = self.table.get_rows(selected=True)[0]
        operation_id = selected_operation.values[0]
        answer = self.toaster.yes_no_box(parent=self, title="delete operation",
                                         message="Are you sure you want to delete this operation")
        if answer == "Yes":
            selected_operation.delete()
            self.api.delete(endpoint=f"operations/delete/{operation_id}/")


