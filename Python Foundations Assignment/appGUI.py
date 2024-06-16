import sys
from PyQt6 import uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView, QMessageBox

from model import Items


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("item_database.ui", self)
        self.build_ui()
        self.show()
        self.error_message = ""
        self.set_default_date()

    def set_default_date(self):
        today = QDate.currentDate()
        self.ui.cal_date_added.setDate(today)
        self.ui.cal_date_added.setDisplayFormat("dd-MM-yyyy")
        self.ui.cal_manufacture_date.setDate(today)
        self.ui.cal_manufacture_date.setDisplayFormat("dd-MM-yyyy")

    def build_ui(self):
        self.ui.btn_add.clicked.connect(self.add_item)
        self.ui.btn_clear.clicked.connect(self.clear_form)
        self.ui.btn_delete.clicked.connect(self.delete_item)
        self.ui.tbl_items.setColumnCount(5)
        self.ui.tbl_items.setHorizontalHeaderLabels(
            ('Title', 'Type', 'Date Added', 'Date of Manufacture', 'Description'))
        self.ui.tbl_items.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.load_items()

    def is_valid_input(self) -> bool:
        is_valid = True
        if not self.ui.txt_title.text():
            self.error_message += "Title cannot be empty.\n"
            is_valid = False
        if not self.ui.txt_description.text():
            self.error_message += "Description cannot be empty.\n"
            is_valid = False
        return is_valid

    def add_item(self):
        if not self.is_valid_input():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Error")
            msg.setText(self.error_message)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            self.error_message = ""
            return

        title = self.ui.txt_title.text()
        item_type = self.ui.cmb_item_type.currentText()
        date_added = self.ui.cal_date_added.date().toPyDate()
        date_manufactured = self.ui.cal_manufacture_date.date().toPyDate()
        description = self.ui.txt_description.text()
        Items(title, item_type, date_added, date_manufactured, description)
        Items.save_to_file()
        self.clear_form()
        self.load_items()

    def clear_form(self):
        self.ui.txt_title.clear()
        self.ui.cmb_item_type.setCurrentIndex(0)
        self.ui.txt_description.clear()
        self.set_default_date()

    def delete_item(self):
        selected_row = self.ui.tbl_items.currentRow()
        if selected_row == -1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("Error")
            msg.setText("No item selected.")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        ask = QMessageBox()
        ask.setIcon(QMessageBox.Icon.Question)
        ask.setWindowTitle("Delete Item")
        ask.setText("Are you sure you want to permanently delete this item?")
        ask.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        ask.activateWindow()
        ret_val = ask.exec()

        if ret_val == QMessageBox.StandardButton.No:
            return

        Items.ITEMS.pop(selected_row)
        Items.save_to_file()
        self.load_items()
        delete_confirmation = QMessageBox()
        delete_confirmation.setWindowTitle("Delete Item")
        delete_confirmation.setText("Item deleted")

    def load_items(self):
        try:
            self.ui.tbl_items.setRowCount(0)
            Items.load_from_file()
            row = 0
            for i in Items.ITEMS:
                self.ui.tbl_items.insertRow(row)
                self.ui.tbl_items.setItem(row, 0, QTableWidgetItem(i.title))
                self.ui.tbl_items.setItem(row, 1, QTableWidgetItem(i.type))
                self.ui.tbl_items.setItem(row, 2, QTableWidgetItem(str(i.date_added)))
                self.ui.tbl_items.setItem(row, 3, QTableWidgetItem(str(i.date_manufactured)))
                self.ui.tbl_items.setItem(row, 4, QTableWidgetItem(i.description))
                row += 1
        except Exception as e:
            # Error handling if loading items fails
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Error loading items from file: " + str(e))
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()


app = QApplication(sys.argv)
w = AppWindow()
sys.exit(app.exec())
