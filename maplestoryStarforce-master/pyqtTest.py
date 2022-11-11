import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import weapon


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 300, 220, 403)
        self.setFixedSize(220, 403)
        self.setWindowTitle("Starforce Simulator")
        # self.setWindowIcon(QIcon("starIcon.png"))

        star=12
        labelItemName = QLabel("아케인셰이드 투핸드소드 ★"+str(star),self)
        labelItemName.setGeometry(5, 2, 300, 20)

        
        
        labelItemImage = QLabel(weapon.twoHandSword,self)
        labelItemImage.setGeometry(10,20,200,250)

        my_font = QFont("Lucida Console", 1)
        labelItemImage.setFont(my_font)


        mesoTotal=format(1234567890, ",")
        labelMesoTotal = QLabel("총 사용 메소 : "+mesoTotal, self)
        labelMesoTotal.setGeometry(8, 219, 300, 100)

        btnStar = QPushButton("강화하기", self)
        btnStar.setGeometry(5, 280, 210, 38)
        btnStar.clicked.connect(self.btnStar_clicked)

        btnStarReset = QPushButton("강화 초기화", self)
        btnStarReset.setGeometry(5, 320, 103, 38)
        btnStarReset.clicked.connect(self.btnStarReset_clicked)

        btnMesoReset = QPushButton("메소 초기화", self)
        btnMesoReset.setGeometry(112, 320, 103, 38)
        btnMesoReset.clicked.connect(self.btnMesoReset_clicked)

        btnQuit = QPushButton("종료하기", self)
        btnQuit.setGeometry(5, 360, 210, 38)
        btnQuit.clicked.connect(self.btnQuit_clicked)
    
    def btnStar_clicked(self):
        print("강화하기 클릭")
        
    def btnStarReset_clicked(self):
        print("강화 초기회 클릭")
    
    def btnMesoReset_clicked(self):
        print("메소 초기화 클릭")
    
    def btnQuit_clicked(self):
        print("종료하기 클릭")

app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()
