import sys
from PyQt5.QtWidgets import *
import sqlite3

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.name = ''
        self.tel = ''
        self.address = ''
        self.bdate = ''
        self.gender = ''

        self.setFixedSize(155, 320)
        self.setWindowTitle('Db')

        self.name_lbl = QLabel('Name Surname', self)
        self.name_ln = QLineEdit(self)
        self.name_ln.setMaxLength(64)
        self.name_lbl.move(10, 10)
        self.name_ln.move(10, 25)

        self.bdate_lbl = QLabel('Date of Birth', self)
        self.bdate_ln = QLineEdit(self)
        self.bdate_ln.setPlaceholderText('15.08.1980')
        self.bdate_ln.setMaxLength(10)
        self.bdate_lbl.move(10, 50)
        self.bdate_ln.move(10, 65)

        self.telno_lbl = QLabel('Tel', self)
        self.telno_ln = QLineEdit(self)
        self.telno_ln.setMaxLength(10)

        self.telno_lbl.move(10, 90)
        self.telno_ln.move(10, 105)

        self.genderLbl = QLabel('Gender', self)
        self.genderLbl.move(10, 130)
        self.genderMale = QRadioButton('Male', self)
        self.genderMale.move(10, 145)
        self.genderFemale = QRadioButton('Female', self)
        self.genderFemale.move(60, 145)

        self.address_lbl = QLabel('Address', self)
        self.address_txt = QTextEdit(self)
        self.address_lbl.move(10, 170)
        self.address_txt.move(10, 185)
        self.address_txt.resize(135, 75)

        self.add = QPushButton('Add to Database', self)
        self.add.move(10, 275)

        self.add.clicked.connect(self.set_name)
        self.add.clicked.connect(self.set_bdate)
        self.add.clicked.connect(self.set_tel)
        self.add.clicked.connect(self.set_gender)
        self.add.clicked.connect(self.set_address)
        self.add.clicked.connect(self.final_check)

    def set_gender(self):
        if self.genderFemale.isChecked():
            self.gender = 'F'
        if self.genderMale.isChecked():
            self.gender = 'M'

    def set_name(self):
        self.name = self.name_ln.text()

    def set_tel(self):
        for i in self.telno_ln.text():
            try:
                self.tel += str(int(i))
            except:
                QMessageBox.warning(self, 'Warning', 'Tel should be all number!')
                self.tel = ''
                return

    def set_bdate(self):
        self.bdate = self.bdate_ln.text()

    def set_address(self):
        if len(self.address_txt.toPlainText()) > 200:
            QMessageBox.warning(self, 'Warning', 'Address should be lesser than 200 characters.')
        else:
            self.address = self.address_txt.toPlainText()

    def final_check(self):
        if not self.name or not self.bdate or not self.address or not self.tel or not self.gender:
            QMessageBox.warning(self, 'Error', 'Invalid input: Failed to add to database!')
        else:
            QMessageBox.information(self, 'Success', '{} successfully added to database!'.format(self.name))
            self.add_to_database()

    def add_to_database(self):
        conn = sqlite3.connect('person.sqlite')
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO info(person_name, person_no, person_address, person_bdate, person_gender) VALUES(?, ?, ?, ?, ?)", (self.name, int(self.tel), self.address, self.bdate, self.gender))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e.args)
            QMessageBox.warning(self, 'Warning', 'Something went very wrong!')
        finally:
            self.name = ''
            self.tel = ''
            self.address = ''
            self.bdate = ''
            self.gender = ''

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()

main()
