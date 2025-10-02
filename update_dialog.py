from PyQt5.QtWidgets import *
from db_helper import DB, DB_CONFIG

class UpdateDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("수정")
        self.db = DB(**DB_CONFIG)

        self.pid = QLineEdit()
        self.pname = QLineEdit()
        self.pprice = QLineEdit()
        self.pinven = QSpinBox()

        form = QFormLayout()
        form.addRow("아이디", self.pid)
        form.addRow("김밥이름", self.pname)
        form.addRow("가격", self.pprice)
        form.addRow("재고", self.pinven)

        
        buttonBox = QHBoxLayout()

        self.btn_submit = QPushButton("수정")
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
        ID = self.pid.text().strip()
        Name = self.pname.text().strip()
        price = self.pprice.text().strip()
        inventory = self.pinven.value()
        if not ID or not Name or not price or not inventory:
            QMessageBox.warning(self, "오류", "데이터를 빠짐없이 입력하세요.")
            return
        ok = self.db.update_items(ID, Name, price, inventory)
        if ok:
            QMessageBox.information(self, "완료", "수정되었습니다.")
        else:
            QMessageBox.critical(self, "실패", "수정 중 오류가 발생했습니다.")
        self.accept()