import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.dialogs.dialogs import Messagebox
from ..app.settings import FONT, SMALL_FONT


class ComboLabelFrame(ttk.Frame):
    def __init__(self, parent, text_varialble, values):
        super(ComboLabelFrame, self).__init__(parent)
        self.label = ttk.Label(
            self, text="Material:", font=f"{FONT} {SMALL_FONT}", justify="left"
        )
        self.label.pack(side="left", anchor="w", padx=20)
        self.combo = ttk.Combobox(
            self,
            values=values,
            textvariable=text_varialble,
            font=f"{FONT} {SMALL_FONT}",
        )
        self.combo.pack(side="right", anchor="e", padx=20)

        self.pack(fill="x", pady=20)


class EntryLabelFrame(ttk.Frame):
    def __init__(self, parent, text, text_variable, show=""):
        super(EntryLabelFrame, self).__init__(parent)
        self.label = ttk.Label(
            self, text=text, font=f"{FONT} {SMALL_FONT}", justify="left"
        )
        self.label.pack(side="left", anchor="w", padx=20)
        self.entry = ttk.Entry(
            self, textvariable=text_variable, show=show, font=f"{FONT} {SMALL_FONT}"
        )
        self.entry.pack(side="right", anchor="e", padx=20)

        self.pack(fill="x", pady=20)


class CheckboxLabelFrame(ttk.Frame):
    def __init__(self, parent, text, variable):
        super(CheckboxLabelFrame, self).__init__(parent)
        self.label = ttk.Label(
            self, text=text, font=f"{FONT} {SMALL_FONT}", justify="left"
        )
        self.label.pack(side="left", anchor="w", padx=20)
        self.entry = ttk.Checkbutton(
            self, variable=variable, onvalue=True, offvalue=False
        )
        self.entry.pack(side="right", anchor="e", padx=20)

        self.pack(fill="x", pady=20)


class Toaster:
    def toast(self, title, message):
        toasty = ToastNotification(title=title, message=message, duration=3000, position=(550, 550, 'ne'))
        toasty.show_toast()

    def yes_no_box(self, parent=None, title="", message=""):
        messagebox = Messagebox()
        answer = messagebox.yesno(title=title, message=message, alert=False, parent=parent)
        return answer

