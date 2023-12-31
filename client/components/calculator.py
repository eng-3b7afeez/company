import ttkbootstrap as ttk
from ..app.settings import FONT, MEDIUM_FONT
from ..utils import ComboLabelFrame, EntryLabelFrame


class Calculator(ttk.Frame):
    def __init__(self, master):
        super(Calculator, self).__init__(master=master)
        self.initialize_vars()
        self.initialize_frames()
        self.calculate_button = ttk.Button(
            self.buttons_frame, text="Calculate", width=15, command=self.calculate
        )
        self.clear_button = ttk.Button(
            self.buttons_frame, text="Clear", width=15, command=self.clear
        )
        self.calculate_button.pack(side="left", anchor="w", padx=20)
        self.clear_button.pack(side="right", anchor="e", padx=20)
        self.buttons_frame.pack(fill="x", padx=50, pady=50)

        self.report_label = ttk.Label(
            self.report_frame,
            textvariable=self.report,
            font=f"{FONT} {MEDIUM_FONT}",
            wraplength=600,
        )
        self.report_label.pack(pady=20)
        self.report_frame.pack(expand=True, fill="both", padx=20, pady=20)

    def initialize_vars(self):
        self.material = ttk.StringVar(value="Material")
        self.material_list = ["Steel", "Stainless", "Aluminium"]
        self.height = ttk.DoubleVar(value=0)
        self.width = ttk.DoubleVar(value=0)
        self.thickness = ttk.DoubleVar(value=0)
        self.report = ttk.StringVar(value="")

    def initialize_frames(self):
        self.material_frame = ComboLabelFrame(
            self,
            text_varialble=self.material,
            values=self.material_list,
        )
        self.height_frame = EntryLabelFrame(
            self, text="Height:", text_variable=self.height
        )
        self.width_frame = EntryLabelFrame(
            self, text="Width:", text_variable=self.width
        )
        self.thickness_frame = EntryLabelFrame(
            self, text="Thickness:", text_variable=self.thickness
        )
        self.buttons_frame = ttk.Frame(self)
        self.report_frame = ttk.LabelFrame(self, text="Report")

    def calculate(self):
        weight = 0
        if not self.material.get() in self.material_list:
            self.report.set(value="Please choose a material")
        elif not self.height.get():
            self.report.set(value="Please provide a height")
        elif not self.width.get():
            self.report.set(value="Please provide a width")
        elif not self.thickness.get():
            self.report.set(value="Please provide a thickness")
        elif self.material.get() == "Steel" or self.material.get() == "Stainless":
            weight = round(
                self.height.get() * self.width.get() * self.thickness.get() * 8, 2
            )
        elif self.material.get() == "Aluminium":
            weight = round(
                self.height.get() * self.width.get() * self.thickness.get() * 2.5, 2
            )
        if weight:
            self.report.set(
                value=f"Material: {self.material.get()}\nHeight: {self.height.get()}\nWidth: {self.width.get()}\nThickness: {self.thickness.get()}\nWeight: {weight}"
            )

    def clear(self):
        self.height.set(value=0)
        self.width.set(value=0)
        self.thickness.set(value=0)
        self.report.set(value="")
