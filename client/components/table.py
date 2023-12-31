from ttkbootstrap.tableview import Tableview


class DataTable(Tableview):
    def __init__(
        self, master,
        coldata,
        rowdata,
        paginated=True,
        pagesize=20,
        searchable=True,
        bootstyle="primary",
        autoalign=False,
        height=50,
    ):
        super(DataTable, self).__init__(
            master=master,
            coldata=coldata,
            rowdata=rowdata,
            paginated=paginated,
            pagesize=pagesize,
            searchable=searchable,
            bootstyle=bootstyle,
            autoalign=autoalign,
            height=height,
        )
        self.hide_selected_column(cid=0)
