from PyQt5.QtWidgets import *
from db_helper import DB, DB_CONFIG

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("추가")
        self.db = DB(**DB_CONFIG)

        self.pname = QLineEdit()
        self.pprice = QLineEdit()
        self.pinven = QSpinBox()

        form = QFormLayout()
        form.addRow("김밥이름", self.pname)
        form.addRow("가격", self.pprice)
        form.addRow("재고", self.pinven)

        buttonBox = QHBoxLayout()

        self.btn_submit = QPushButton("추가")
        self.btn_submit.clicked.connect(self.submit)
        self.btn_cancel = QPushButton("취소")
        self.btn_cancel.clicked.connect(self.reject)

        buttonBox.addWidget(self.btn_submit)
        buttonBox.addWidget(self.btn_cancel)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(buttonBox)
        self.setLayout(layout)

    def submit(self):
        Name = self.pname.text().strip()
        price = self.pprice.text().strip()
        inventory = self.pinven.value()
        if not Name or not price or not inventory:
            QMessageBox.warning(self, "오류","데이터를 빠짐없이 입력하세요.")
            return
        ok = self.db.insert_items(Name, price, inventory)
        if ok:
            QMessageBox.information(self,"완료","추가되었습니다.")
        else:
            QMessageBox.critical(self,"실패","추가 중 오류가 발생했습니다.")
        self.accept()