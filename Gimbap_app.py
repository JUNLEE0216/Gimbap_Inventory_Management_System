import sys
from PyQt5.QtWidgets import QApplication
from inventory_gui import InventoryWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryWindow()
    window.show()
    sys.exit(app.exec_())