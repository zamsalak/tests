import sys
from PyQt5.QtWidgets import *

iller = {
    'İstanbul': {'Esenyurt': 846492, 'Küçükçekmece': 770393, 'Bağcılar': 748483, 'Ümraniye': 699901, 'Pendik': 698260, 'Bahçelievler': 598454},
    'Ankara': {'Çankaya': 921999, 'Keçiören': 917759, 'Yenimahalle': 659603, 'Mamak': 637935, 'Etimesgut': 566500, 'Sincan': 524222},
    'İzmir': {'Buca': 492252, 'Karabağlar': 480790},
    'Bursa': {'Osmangazi': 856770, 'Yıldırım': 647520}
}


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(285, 295)
        self.setWindowTitle('Population')

        self.cityLabel = QLabel('<b>City</b>', self)
        self.cityLabel.move(10, 10)

        self.lwCity = QListWidget(self)
        self.lwCity.move(10, 30)
        self.lwCity.resize(125, 200)

        self.districtLabel = QLabel('<b>District</b>', self)
        self.districtLabel.move(150, 10)

        self.lwDistrict = QListWidget(self)
        self.lwDistrict.move(150, 30)
        self.lwDistrict.resize(125, 200)

        self.quitButton = QPushButton('Quit', self)
        self.quitButton.move(200, 250)

        for i in iller:
            self.lwCity.addItem(i)

        self.lwCity.itemDoubleClicked.connect(self.illerDoubleClicked)
        self.lwCity.itemClicked.connect(self.singleClicked)
        self.lwDistrict.itemDoubleClicked.connect(self.ilcelerDoubleClicked)
        self.quitButton.clicked.connect(self.quitButtonHandler)

    def singleClicked(self, item):
        self.lwDistrict.clear()
        for i in iller[item.text()]:
            self.lwDistrict.addItem(i)

    def quitButtonHandler(self):
        self.close()

    def illerDoubleClicked(self, item):
        total = 0   #ilçelerin nüfus toplamı, ilin nüfusunu verdiği için bu şekilde yaptım. Tabii, tüm ilçeler dahil edilmediğinden sonuç yanıl çıkacaktır.
        for il in iller[item.text()]:
            total += iller[item.text()][il]
        QMessageBox.information(self, 'Population',  'Population of ' + item.text() + ' is: '+ '{:,}'.format(total))

    def ilcelerDoubleClicked(self, item):
        population = iller[self.lwCity.currentItem().text()][item.text()]
        QMessageBox.information(self, 'Population', 'Population of ' + item.text() + ' is: ' + '{:,}'.format(population))



def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()

main()
