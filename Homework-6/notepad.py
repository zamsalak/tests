import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import mainScreen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main = mainScreen.Ui_MainWindow()
        self.ui_main.setupUi(self)

        self.file = None
        self.saved = False
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.ui_main.actionOpen.triggered.connect(self.actionOpenTriggered)
        self.ui_main.actionQuit.triggered.connect(self.actionQuitTriggered)
        self.ui_main.actionSave.triggered.connect(self.actionSaveTriggered)
        self.ui_main.actionSave_As.triggered.connect(self.actionSave_AsTriggered)
        self.ui_main.actionFont.triggered.connect(self.actionFontTriggered)
        self.ui_main.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

    def actionOpenTriggered(self):
        fileDialog = QFileDialog(self, 'Dosya Seçiniz')
        fileDialog.setNameFilter('Text Files (*.txt)')

        if fileDialog.exec() == QDialog.Accepted:
            self.setWindowTitle(fileDialog.selectedFiles()[0])
            self.file = fileDialog.selectedFiles()[0]
            with open(fileDialog.selectedFiles()[0], 'r') as f:
                self.ui_main.textEdit.setPlainText(f.read())

    def _wantToSave(self):
        msg = QMessageBox.warning(self, 'Exiting', 'Do you want to save last changes?',
                                  QMessageBox.Save | QMessageBox.Cancel)
        return True if msg == 2048 else False

    def actionQuitTriggered(self):
        if self.file is not None:
            if self.saved is False:
                if self._wantToSave():
                    self.actionSaveTriggered()
                else:
                    self.close()
        elif self.file is None:
            if self.ui_main.textEdit.toPlainText() != '':
                if self._wantToSave():
                    self.actionSave_AsTriggered()
                else:
                    self.close()
        self.close()
    #-------Backup---------
    # def actionQuitTriggered(self):
    #     if self.file is not None:
    #         if self.saved is False:
    #             msg = QMessageBox.warning(self, 'Exiting', 'Do you want to save last changes?', QMessageBox.Save | QMessageBox.Cancel)
    #             if msg == 2048:
    #                 self.actionSaveTriggered()
    #             elif msg == 4194304:
    #                 self.close()
    #     elif self.file is None:
    #         if self.ui_main.textEdit.toPlainText() != '':
    #
    #             self.actionSave_AsTriggered()
    #
    #     self.close()

    def actionSaveTriggered(self):
        if self.file is not None and self.saved is False:
            with open(self.file, 'r+') as f:
                f.write(self.ui_main.textEdit.toPlainText())
                self.saved = True
                self.statusMessageSaved()
        elif self.file is None and self.ui_main.textEdit.toPlainText() != '':
            self.actionSave_AsTriggered()
        else:
            return

    def actionSave_AsTriggered(self):
        path = QFileDialog.getSaveFileName(self, 'Dizin', '.', 'Text Files(*.txt);;All Files(*.*)')
        if path[0] != '' and self.saved is False:
            self.file = path[0]
            with open(self.file, 'w') as f:
                f.write(self.ui_main.textEdit.toPlainText())
                self.saved = True
                self._statusMessageSaved()

    def actionFontTriggered(self):
        font = QFontDialog.getFont()[0]
        self.ui_main.textEdit.setFont(font)
        self.statusBar.showMessage('Saved!')

    def statusMessageSaved(self):
        self.statusBar.showMessage('%s is saved!' % self.file, 3000)

    def closeEvent(self, event):
        self.actionQuitTriggered()


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()


if __name__ == '__main__':
    main()
