from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from db_helper import DB, DB_CONFIG
from insert_dialog import InsertDialog
from update_dialog import UpdateDialog
from delete_dialog import DeleteDialog

class InventoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("김밥 재고 관리")
        self.setWindowIcon(QIcon("Gimbap.png"))
        self.resize(400,300)

        self.db = DB(**DB_CONFIG)

        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        form_box = QHBoxLayout()
        self.btn_insert = QPushButton("추가")
        self.btn_update = QPushButton("수정")
        self.btn_delete = QPushButton("삭제")

        self.btn_insert.clicked.connect(self.open_dialog_insert)
        self.btn_update.clicked.connect(self.open_dialog_update)
        self.btn_delete.clicked.connect(self.open_dialog_delete)

        form_box.addWidget(self.btn_insert)
        form_box.addWidget(self.btn_update)
        form_box.addWidget(self.btn_delete)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "김밥", "가격", "재고"])
        self.table.setEditTriggers(self.table.NoEditTriggers) 
        self.table.verticalHeader().setVisible(False)

        vbox.addLayout(form_box)
        vbox.addWidget(self.table)
        self.load_items()

    def load_items(self):
        rows = self.db.fetch_items()
        self.table.setRowCount(len(rows))
        for r, (ID, Name, price, inventory) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(ID)))
            self.table.setItem(r, 1, QTableWidgetItem(Name))
            self.table.setItem(r, 2, QTableWidgetItem(str(int(price))))
            self.table.setItem(r, 3, QTableWidgetItem(str(inventory)))
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    def open_dialog_insert(self) :
        dialog = InsertDialog()
        if dialog.exec_() == InsertDialog.Accepted :
            self.load_items()
    
    def open_dialog_update(self) :
        dialog = UpdateDialog()
        if dialog.exec_() == UpdateDialog.Accepted :
            self.load_items()
            
    def open_dialog_delete(self) :
        dialog = DeleteDialog()
        if dialog.exec_() == DeleteDialog.Accepted :
            self.load_items()

