import ttkbootstrap as ttk
from .calculator import Calculator


class Side(ttk.Frame):
    def __init__(self, master):
        super(Side, self).__init__(master=master)
        self.frame = ttk.LabelFrame(self, text="Forms")
        self.frame.pack(fill="both", expand=True)
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=20)
        self.calculator = Calculator(self.notebook)
        self.calculator.pack(fill="both", expand=True)
        self.notebook.add(self.calculator, text="Calculator")
