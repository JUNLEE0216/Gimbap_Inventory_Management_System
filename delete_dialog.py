from PyQt5.QtWidgets import *
from db_helper import DB, DB_CONFIG

class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("삭제")
        self.db = DB(**DB_CONFIG)

        self.pid = QLineEdit()

        form = QFormLayout()
        form.addRow("아이디", self.pid)

        buttonBox = QHBoxLayout()

        self.btn_submit = QPushButton("삭제")
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
        if not ID:
            QMessageBox.warning(self, "오류", "데이터를 빠짐없이 입력하세요.")
            return
        ok = self.db.delete_items(ID)
        if ok:
            QMessageBox.information(self, "완료", "삭제되었습니다.")
        else:
            QMessageBox.critical(self, "실패", "삭제 중 오류가 발생했습니다.")
        self.accept()