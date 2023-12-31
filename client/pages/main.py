import ttkbootstrap as ttk
from .customers import Customers
from .operations import Operations


class Main(ttk.Frame):
    def __init__(self, parent, api):
        super(Main, self).__init__(master=parent)
        self.api = api
        self.frame = ttk.LabelFrame(self, text="Body")
        self.frame.pack(fill="both", expand=True)
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=20)
        self.customers = Customers(
            self.notebook, api=self.api
        )
        self.customers.pack(fill="both", expand=True)
        self.operations = Operations(
            self.notebook, api=self.api
        )
        self.operations.pack(fill="both", expand=True)
        self.notebook.add(self.customers, text="Customers")
        self.notebook.add(self.operations, text="Operations")
